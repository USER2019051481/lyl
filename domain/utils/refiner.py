from z3 import *


class Refiner:
    def __init__(self, vi):
        self.vi = vi

    def generate_dnf_model(self, model_arr):
        def dfs(idx, tmp_list):
            if idx >= len(or_clause):
                this_is_a_list.append(list(tmp_list))
                return
            for expr in or_clause[idx]:
                tmp_list.append(expr)
                dfs(idx + 1, tmp_list)
                tmp_list.pop()

        res = []
        for or_clause in model_arr:
            this_is_a_list = []
            dfs(0, [])
            res.extend(this_is_a_list)
        return res

    def detect_contradiction(self, res, feasible_region=True):
        res_without_contra = []
        for clause in res:
            s = Solver()
            s.add(*clause, feasible_region)
            if s.check() == sat:
                res_without_contra.append(clause)
        return res_without_contra

    def detect_implic(self, res):
        def imply(expr1, expr2):
            s = Solver()
            s.add(ForAll(self.vi, Implies(expr1, expr2)))
            return s.check() == sat

        res_without_implic = []
        for clause in res:
            imply_matrix = [[False for _ in range(len(clause))] for _ in range(len(clause))]
            for i in range(len(clause)):
                for j in range(len(clause)):
                    if i != j and not imply_matrix[j][i]:
                        imply_matrix[i][j] = imply(clause[i], clause[j])
            for i in range(len(clause)):
                for j in range(len(clause)):
                    if imply_matrix[i][j]:
                        clause[j] = None
            res_without_implic.append([expr for expr in clause if expr is not None])
        return res_without_implic

    def detect_union(self, res):
        def exist_union(expr1, expr2):
            s = Solver()
            s.add(expr1, expr2)
            return s.check() == sat

        res_without_union = []
        for i in range(len(res)):
            expr1 = And(*res[i])
            for j in range(i):
                expr2 = And(*res[j])
                if exist_union(expr1, expr2):
                    res[i].append(Not(expr2))
            res_without_union.append(res[i])
        return res_without_union

    def refine(self, model_arr, feasible_region):
        print('----------Original Model----------')
        print('Or:')
        for c1 in model_arr:
            print('\tAnd:')
            for c2 in c1:
                print('\t\tOr:')
                for c3 in c2:
                    print('\t\t\t', c3)

        res = self.generate_dnf_model(model_arr)
        print('-' * 10, 'DNF model', '-' * 10)
        print('Or:')
        for c1 in res:
            print('\tAnd:')
            for c2 in c1:
                print('\t\t', c2)

        res_without_contra = self.detect_contradiction(res, feasible_region)
        print('-' * 10, 'No Nontradiction', '-' * 10)
        print('Or:')
        for c1 in res_without_contra:
            print('\tAnd:')
            for c2 in c1:
                print('\t\t', c2)

        res_without_implic = self.detect_implic(res_without_contra)
        print('-' * 10, 'No Implication', '-' * 10)
        print('Or:')
        for c1 in res_without_implic:
            print('\tAnd:')
            for c2 in c1:
                print('\t\t', c2)

        # res_without_union = self.detect_union(res_without_implic)
        # print('-' * 10, 'No Union', '-' * 10)
        # print('Or:')
        # for c1 in res_without_union:
        #     print('\tAnd:')
        #     for c2 in c1:
        #         print('\t\t', c2)
        #
        # return res_without_union

        return res_without_implic

    def simplify_dnf_model_arr(self, model):
        no_contra = self.detect_contradiction(model)
        no_implic = self.detect_implic(no_contra)
        return no_implic


if __name__ == '__main__':
    v1, v2 = Int('v1'), Int('v2')
    model = [[[1 * v1 + 1 * v2 < 4, 1 * v1 + 1 * v2 == 4],
              [1 * v1 + 1 * v2 < 3, 1 * v1 + 1 * v2 == 3],
              [(2 * v1 + 0 * v2) % 4 == 1, (2 * v1 + 0 * v2) % 4 == 2, (2 * v1 + 0 * v2) % 4 == 3]],
             [[1 * v1 + 1 * v2 == 4],
              [1 * v1 + 1 * v2 < 3],
              [(2 * v1 + 0 * v2) % 4 == 1, (2 * v1 + 0 * v2) % 4 == 2, (2 * v1 + 0 * v2) % 4 == 3]]]
    refiner = Refiner([v1, v2])

    res_without_union = refiner.refine(model, True)
    print(res_without_union)
    print('-' * 50)
    model = [[Not((5 * v1 + 1 * v2) % 6 == 0), Not((3 * v1 + 3 * v2) % 5 == 1)],
             [Not((5 * v1 + 1 * v2) % 6 == 0), Not((3 * v1 + 3 * v2) % 5 == 1)]]
    simplied_model = refiner.simplify_dnf_model_arr(model)
    print(simplied_model)

    model = [[v1 % 2 == 0], [v2 % 2 == 0]]
    res = refiner.detect_union(model)
    print(res)
