from z3 import *
from domain.utils.analyse_snt import analyse_snt_z3, analyse_snt_bool


class Action: #解析动作，k==1 ， k == 2
    def __init__(self, word_list, var_mapper, eff_mapper):
        self.name = word_list[0]

        ptr = 1
        task_dict = {"name": self.name}
        while ptr < len(word_list):
            word = word_list[ptr]
            if word[0] == ':':
                task_dict[word[1:]] = word_list[ptr + 1]
                ptr += 2

        for k, v in task_dict.items():
            print("%s : %s" % (k, v))

        self.var_mapper = var_mapper
        self.eff_mapper = eff_mapper
        self.params_mapper = {}
        self.precondition = None
        self.precond_list = task_dict["precondition"]
        self.effect_list = []

        print("analysing parameters:")
        self._analyse_params(task_dict["parameters"])
        print("\tparameters mapper:", self.params_mapper) #take_k_0

        print("analysing precondition:")
        self._analyse_precondition(task_dict["precondition"])
        print("\t", self.precondition)
        # print("\t", self.precond_list)

        print("analysing effect:")
        self.effect_list = self._analyse_effect(task_dict["effect"])
        visited = {eff[1] for eff in self.effect_list}
        keys = {k for k in self.var_mapper}
        for var in keys.difference(visited):
            self.effect_list.append([True, var, var])
        print("\t", self.effect_list)

        print("-" * 50)

    def _analyse_params(self, params_list):
        for i, param in enumerate(params_list):
            icg_var = Int("%s_k_%d" % (self.name, i))
            self.params_mapper[param] = icg_var

    def _mapper(self, key: str):
        if key[0] == '?':
            if key in self.var_mapper:
                return self.var_mapper[key]
            elif key in self.params_mapper:
                return self.params_mapper[key]
            elif key in self.eff_mapper:
                return self.eff_mapper[key]
            else:
                raise RuntimeError("Variable %s doesn't exists!" % key)
        return int(key)

    def _analyse_precondition(self, pre_list):
        self.precondition = analyse_snt_z3(pre_list, self._mapper)
        # op_mapper = {'=': '=', '>': '<', '<': '>', '<=': '>=', '>=': '<='}
        # def format_precond(word_list: list):
        #     for word in word_list:
        #         if type(word) == list:
        #             format_precond(word)
        #     if word_list[0] in op_mapper:
        #         if type(word_list[2]) is not list and word_list[2] in self.params_mapper:
        #             word_list[0] = op_mapper[word_list[0]]
        #             word_list[1], word_list[2] = word_list[2], word_list[1]
        # format_precond(self.precond_list)

    def _analyse_effect(self, effect_list):
        if effect_list[0] == 'and':
            return [self._analyse_effect(words)[0] for words in effect_list[1:]]
        elif effect_list[0] == 'assign':
            return [[True, effect_list[1], effect_list[2]]]
        elif effect_list[0] == 'when':
            return [[effect_list[1], *effect_list[2][1:]]]
        else:
            raise RuntimeError("operator '%s' unrecognized" % effect_list[0])

    def trans_formula(self):
        trans_f = self.precondition
        for eff in self.effect_list:
            assert len(eff) == 3
            eff_var = self.eff_mapper[eff[1]]
            assign = analyse_snt_z3(eff[2], self._mapper)
            if eff[0] is True:
                trans_f = And(trans_f, eff_var == assign)
            else:
                cond = analyse_snt_z3(eff[0], self._mapper)
                trans_f = And(trans_f, If(cond, eff_var == assign, eff_var == self.var_mapper[eff[1]]))
        return simplify(trans_f)

    def get_eff(self, var_dict, param_dict):
        def mapper(key):
            if key[0] == '?':
                if key in var_dict:
                    return var_dict[key]
                elif key in param_dict:
                    return param_dict[key]
                else:
                    raise RuntimeError("Variable %s doesn't exists!" % key)
            else:
                return int(key)

        if analyse_snt_bool(self.precond_list, mapper):
            eff_dict = {k: v for k, v in var_dict.items()}
            for eff in self.effect_list:
                if eff[0] is True:
                    eff_dict[eff[1]] = analyse_snt_bool(eff[2], mapper)
                elif analyse_snt_bool(eff[0], mapper):
                    eff_dict[eff[1]] = analyse_snt_bool(eff[2], mapper)
            return eff_dict
        else:
            return None

    def get_all_params(self, var_dict):
        """
        该方法用于求解action中，自由变量k的所有取值
        """

        def mapper(key):
            if key[0] == '?':
                if key in var_dict:
                    return var_dict[key]
                elif key in self.params_mapper:
                    return self.params_mapper[key]
                else:
                    raise RuntimeError("Variable %s doesn't exists!" % key)
            else:
                return int(key)

        k_set = set()
        k = list(self.params_mapper.keys())[0]
        # print("keys=\n",self.params_mapper.keys())
        precond = analyse_snt_z3(self.precond_list, mapper)
        if str(precond) == 'True':
            return None, None, True
        elif str(precond) == 'False':
            return None, None, False

        s = Solver()
        s.add(precond)
        while s.check() == sat:
            # print('s:', s)
            # print('model:', s.model())
            param = s.model()[self.params_mapper[k]].as_long()
            k_set.add(param)
            s.add(self.params_mapper[k] != param)

        #k是数值  1，2 ；k_set是 k，1，2，true
        return k, k_set, True

        # res_params = {k: [] for k in self.params_mapper}
        # if self.precond_list[0] == 'and':
        #     params_range_of_each_clause = {k: [0, 1 << 32] for k in self.params_mapper}
        #     for snt_list in self.precond_list[1:]:
        #         if snt_list[1] in self.params_mapper:
        #             res = analyse_snt_bool(snt_list[2], mapper)
        #             param = snt_list[1]
        #             if snt_list[0] == '=':
        #                 params_range_of_each_clause[param] = [res, res]
        #             elif snt_list[0] == '<':
        #                 up = params_range_of_each_clause[param][1]
        #                 up = min(up, res - 1)
        #                 params_range_of_each_clause[param][1] = up
        #             elif snt_list[0] == '<=':
        #                 up = params_range_of_each_clause[param][1]
        #                 up = min(up, res)
        #                 params_range_of_each_clause[param][1] = up
        #             elif snt_list[0] == '>':
        #                 bottom = params_range_of_each_clause[param][0]
        #                 bottom = max(bottom, res + 1)
        #                 params_range_of_each_clause[param][0] = bottom
        #             elif snt_list[0] == ">=":
        #                 bottom = params_range_of_each_clause[param][0]
        #                 bottom = max(bottom, res)
        #                 params_range_of_each_clause[param][0] = bottom
        #
        #     for k, v in params_range_of_each_clause.items():
        #         res_params[k].append(v)
        # elif self.precond_list[0] == 'or':
        #     # 该部分尚未开发
        #     raise RuntimeError("Function under developing...")
        # elif self.precond_list[0] == '=':
        #     res_params[self.precond_list[1]].append(
        #         analyse_snt_bool(self.precond_list[2], mapper))
        # return res_params


if __name__ == '__main__':
    word_list = ['take1',
                  ':parameters', ['?k'],
                  ':precondition', ['or', ['and', ['=', '?k', '1'], ['>', '?v1', '0']], ['and', ['=', '?k', '2'], ['>', '?v1', '1']]],
                  ':effect', ['assign', '?v1', ['-', '?v1', '?k']]]
    var_mapper = {'?v1': Int('v0'), '?v2': Int('v1')}
    eff_mapper = {k: Int("w%d" % i) for i, k in enumerate(var_mapper)}
    action = Action(word_list, var_mapper, eff_mapper)
    print(action.get_all_params({'?v1': 3, '?v2': 5}))
