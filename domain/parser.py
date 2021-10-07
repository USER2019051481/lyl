from z3 import Int, And, Or, Exists, simplify
from domain.utils.split import split
from domain.utils.analyse_snt import analyse_snt_z3
from domain.action import Action


# PDDL文件解析器
class PDDLParser:
    def __init__(self, pddl_pwd):
        self.pddl2icg = {}
        self.eff_mapper = {}
        self.constant_mapper = {}
        # self.variables = []
        self.ending_states = []
        self.constraints = None
        self.actions = []
        self.feasible_region = None

        lines = []
        for line in open(pddl_pwd):
            lines.append(line.strip())
        pddl_ln = ' '.join(lines)
        pddl_tasks = split(pddl_ln)

        print("Preliminary analyse:")
        for task in pddl_tasks:
            print(task)
        print("/" * 50)

        task_dict = {"action": []}
        for task in pddl_tasks:
            if task[0][0] == ':':
                key = task[0][1:]
                if key == 'action':
                    task_dict[key].append(task[1:])
                else:
                    task_dict[key] = task[1:]
            else:
                if task[0] == 'domain':
                    self.name = task[1]
        print(self.name)

        print("Turning into task_dict:")
        for k, v in task_dict.items():
            print("%s: %s" % (k, v))
        print("/" * 100)

        if "constants" in task_dict:
            print("Analysing constants:")
            self._analyse_constants(task_dict["constants"])
            print(self.constant_mapper)
            self._replace_constant(task_dict["tercondition"])
            self._replace_constant(task_dict["constraint"])
            self._replace_constant(task_dict["action"])
            print("/" * 50)

        print("Analysing objects:")
        self._analyse_objects(task_dict["objects"])
        self.eff_mapper = {k: Int("w%d" % i) for i, k in enumerate(self.pddl2icg)}
        print("variable mapper(pddl2icg):", self.pddl2icg)
        # print("variables:", self.variables)
        print("/" * 50)

        print("Analysing ending states:")
        states = self._analyse_tercondition(task_dict["tercondition"][0])
        if type(states) == list:
            self.ending_states.extend(states)
        else:
            self.ending_states.append(states)
        print(self.ending_states)
        print("/" * 50)

        print("Analysing feasible region:")
        self.feasible_region = self._feasible_region(task_dict["constraint"][0])
        print(self.feasible_region)
        print("/" * 50)


        print("Analysing constraint:")
        self.constraints = self._analyse_constraint(task_dict["constraint"][0])
        print(self.constraints)
        print("/" * 50)

        print("Analysing actions:")
        self.actions.extend(self._analyse_action(task_dict["action"]))
        print("/" * 100)

    def _analyse_constants(self, arr):
        self.constant_mapper = {arr[i]: arr[i + 1] for i in range(0, len(arr), 2)}

    def _replace_constant(self, arr):
        for i, elem in enumerate(arr):
            if type(elem) == list :
                self._replace_constant(elem)
            elif elem in self.constant_mapper:
                    arr[i] = self.constant_mapper[elem]

    def _analyse_objects(self, arr):
        # 解析PDDL中的变量，将其转化为Z3的变量，用列表按序存储
        for i, pddl_var in enumerate(arr):
            icg_var = Int("v%d" % i)
            # self.variables.append(icg_var)
            self.pddl2icg[pddl_var] = icg_var

    def _analyse_tercondition(self, arr):
        # 该方法目前只支持解析And()型语句以及直接赋值的语句
        if arr[0] == '=':
            return {arr[1]: int(arr[2])}
        assert arr[0] == 'and'
        if arr[0] == 'and':
            ending_state_mapper = dict()
            for state in arr[1:]:
                ending_state_mapper[state[1]] = int(state[2])
            return ending_state_mapper

    def _analyse_constraint(self, word_list):
        def mapper1(key):
            if key in self.pddl2icg:
                return self.pddl2icg[key]
            else:
                return int(key)

        def mapper2(key):
            if key in self.eff_mapper:
                return self.eff_mapper[key]
            else:
                return int(key)

        const = And(analyse_snt_z3(word_list, mapper1), analyse_snt_z3(word_list, mapper2))
        return simplify(const)

    def _analyse_action(self, action_list):
        return [Action(snt, self.pddl2icg, self.eff_mapper) for snt in action_list]

    def _feasible_region(self, word_list):
        def mapper(key):
            if key in self.pddl2icg:
                return self.pddl2icg[key]
            else:
                return int(key)

        return analyse_snt_z3(word_list, mapper)

    def transition_formula(self):
        trans = False
        for act in self.actions:
            trans = Or(trans, Exists(list(act.params_mapper.values()), act.trans_formula()))
            print("trans:\n",trans)
        return simplify(trans)


if __name__ == '__main__':
    i1 = PDDLParser("./pddl/Chomp_game.pddl")
    print(i1.transition_formula())

    var_dict = {"?v1": 5, "?v2": 6}
    param_dict = {"?k": 2}
    print(var_dict, i1.actions[0].get_eff(var_dict, param_dict), i1.actions[0].get_all_params(var_dict))
    print(var_dict, i1.actions[1].get_eff(var_dict, param_dict), i1.actions[1].get_all_params(var_dict))

    var_dict = {"?v1": 5, "?v2": 2}
    param_dict = {"?k": 4}
    print(var_dict, i1.actions[0].get_eff(var_dict, param_dict), i1.actions[0].get_all_params(var_dict))
    print(var_dict, i1.actions[1].get_eff(var_dict, param_dict), i1.actions[1].get_all_params(var_dict))


##########################3
