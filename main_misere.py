from domain.parser import PDDLParser
from generator import MisereGenerator
from z3 import simplify
import time
import os

if __name__ == '__main__':
    start = time.time()
    # domain = PDDLParser("./pddl/Empty_and_divide.pddl")
    # domain = PDDLParser("./pddl/Four-piled-End-nim-v4le1.pddl")
    # domain = PDDLParser("./pddl/Four-piled-small-nim-v4le1.pddl")
    # domain = PDDLParser("./pddl/Monotonic-4-piled-Nim-v4le1.pddl") #dui
    # domain = PDDLParser("./pddl/Odd-Z-indepent-vectors(n=3,v_3-1).pddl")
    # domain = PDDLParser("./pddl/t,d-i-Mark-Game{2,2}.pddl") #dui
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{2,4}.pddl") #dui ， 13s
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{2,6}.pddl") #dui。19s
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{2,8}.pddl") #dui
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{3,2}.pddl") #dui
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{3,3}.pddl")
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{3,5}.pddl")
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{4,3}.pddl")
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{6,3}.pddl")
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{9,9}.pddl")
    # domain = PDDLParser("./pddl/Three-piled-1-slow-nimv3-1.pddl") #dui ，1s
    # domain = PDDLParser("./pddl/Three-piled-1-slow-nimv3-2.pddl") #dui，0.4s
    # domain = PDDLParser("./pddl/Three-piled-1-slow-nimv3-3.pddl") #dui ，2s
    # domain = PDDLParser("./pddl/Three-piled-End-nim.pddl")
    # domain = PDDLParser("./pddl/Three-piled-Greedy_NIm.pddl")
    # domain = PDDLParser("./pddl/Three-piled-nim(v3-le-2).pddl")
    # domain = PDDLParser("./pddl/Three-piled-nim(v3-le-1).pddl")
    # domain = PDDLParser("./pddl/Three-piled-nim(v3-le-3).pddl")
    #
    # domain = PDDLParser("./pddl/Two-piled-1-slow-nim.pddl") #dui，0.2s
    # domain = PDDLParser("./pddl/Two-piled-2-slow-nim.pddl") #dui，5s
    # domain = PDDLParser("./pddl/Two-piled-3-slow-nim.pddl") #dui，1s
    # domain = PDDLParser("./pddl/Two-piled-4-slow-nim.pddl") #dui ，19s
    # domain = PDDLParser("./pddl/Two-piled-5-slow-nim.pddl") #dui，32s
    # domain = PDDLParser("./pddl/Two-piled-6-slow-nim.pddl") #dui
    # domain = PDDLParser("./pddl/Two-piled-7-slow-nim.pddl") #dui，了。
    # domain = PDDLParser("./pddl/Two-piled-8-slow-nim.pddl") #dui
    # domain = PDDLParser("./pddl/Two-piled-9-slow-nim.pddl")  # dui
    # 10不行，跳走了e=11那个参数，看一下是哪一步出现了问题，改一下
    # domain = PDDLParser("./pddl/Two-piled-12-slow-nim.pddl")
    # domain = PDDLParser("./pddl/Two-piled-30-slow-nim.pddl")  #超时

    # domain = PDDLParser("./pddl/Two-piled-End-nim.pddl") #dui
    # domain = PDDLParser("./pddl/Two-piled-Small_NIm.pddl")
    # domain = PDDLParser("./pddl/Two-piled-small_NIm.pddl") #dui
    # domain = PDDLParser("./pddl/Two-staircase.pddl") #dui

    # domain = PDDLParser("./pddl/Empty_and_divide.pddl") #等
    # domain = PDDLParser("./pddl/two_piled_nim.pddl")  #（对）4
    # domain = PDDLParser("./pddl/Chomp_game.pddl") #（对）4
    # domain = PDDLParser("./pddl/L_shaped_chomp_game.pddl") #（ dui）4
    # domain = PDDLParser("./pddl/Monotonic_2_piled_nim.pddl")#（ dui）4
    # domain = PDDLParser("./pddl/monotic_2_diet_wythoff.pddl") #(dui)4
    # domain = PDDLParser("./pddl/monotonic_2_piled_wythoff_game.pddl") #(Dui)4
    # domain = PDDLParser("./pddl/Take_Away.pddl")  #(对）3
    # domain = PDDLParser("./pddl/Subtraction_game.pddl") #获取地址，PDDLParser是PDDL解析器 #（对）4

    # domain = PDDLParser("./pddl/Take-away-2.pddl") #(对）4
    # domain = PDDLParser("./pddl/Take-away-3.pddl")  #（对）4
    # domain = PDDLParser("./pddl/Take-away-4.pddl") #(dui)4
    # domain = PDDLParser("./pddl/Take-away-5.pddl")#(dui)4
    # domain = PDDLParser("./pddl/Take-away-6.pddl") #(dui)3
    # domain = PDDLParser("./pddl/Take-away-7.pddl") #(dui)3
    # domain = PDDLParser("./pddl/Take-away-8.pddl")   #dui
    # domain = PDDLParser("./pddl/Take-away-9.pddl") #dui
    # domain = PDDLParser("./pddl/Take-away-10.pddl") #dui
    # domain = PDDLParser("./pddl/Take-away-11.pddl")#dui
    # domain = PDDLParser("./pddl/Take-away-13.pddl") #dui
    # domain = PDDLParser("./pddl/Take-away-12.pddl") #dui
    # domain = PDDLParser("./pddl/Take-away-15.pddl") #dui

    # domain = PDDLParser("./pddl/Take-away-20.pddl")
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{4,2}.pddl")

    # domain = PDDLParser("./pddl/L_shaped_chomp_game.pddl") #dui
    # domain = PDDLParser("./pddl/I-Mark-Game{{1,2},2}.pddl") #dui
    # domain = PDDLParser("./pddl/Four-piled-small-nim-v4le1.pddl") #dui
    # domain = PDDLParser("./pddl/Four-piled-End-nim-v4le1.pddl") #

    # domain = PDDLParser("./pddl/Monotonic-2-piled-Nim.pddl") #对1
    # domain = PDDLParser("./pddl/Monotonic-3-piled-Nim.pddl")#dui1
    # domain = PDDLParser("./pddl/Monotonic-4-piled-Nim-v4le1.pddl") #dui
    # domain = PDDLParser("./pddl/t,d-i-Mark-Game{2,2}.pddl")#dui
    # domain = PDDLParser("./pddl/T,d-I-Mark-Game{2,4}.pddl") #对

    # domain = PDDLParser("./pddl/Three-piled-Greedy_NIm.pddl")
    # domain = PDDLParser("./pddl/Three-piled-End-nim.pddl")
    #
    # domain = PDDLParser("./pddl/Two-piled-3-slow-nim.pddl")#dui4
    # domain = PDDLParser("./pddl/Two-piled-End-nim.pddl") #dui
    # domain = PDDLParser("./pddl/Two-piled-Greedy_NIm.pddl")#dui4
    # domain = PDDLParser("./pddl/Two-piled-Small_NIm.pddl") #dui
    #
    # domain = PDDLParser("./pddl/Two-piled-Greedy_NIm.pddl") #对

    ##Subtraction_game
    # domain = PDDLParser("./pddl/Subtraction-(1).pddl") #DUI
    # domain = PDDLParser("./pddl/Subtraction-(2).pddl") #dui
    # domain = PDDLParser("./pddl/Subtraction-(3).pddl") # DUI
    # domain = PDDLParser("./pddl/Subtraction-(4).pddl")

    # domain = PDDLParser("./pddl/Subtraction-(2,3).pddl") #dui

    # domain = PDDLParser("./pddl/Subtraction-(1,2).pddl")#dui
    # domain = PDDLParser("./pddl/Monotonic-2-Diet-wythoff-game.pddl") #dui
    # domain = PDDLParser("./pddl/Wythoff-v1-1.pddl") #dui
    # domain = PDDLParser("./pddl/Wythoff-v1-2.pddl") #dui
    # domain = PDDLParser("./pddl/Subtraction-(1,3,4,10).pddl")
    # domain = PDDLParser("./pddl/Subtraction-(1,3,5,10).pddl")
    # domain = PDDLParser("./pddl/Subtraction-(1,3,7,10).pddl")

    # domain = PDDLParser("./pddl/Monotonic_wythoff_game.pddl") #dui1ban
    # domain = PDDLParser("./pddl/Monotonic-6-Diet-wythoff-game.pddl")
    # domain = PDDLParser("./pddl/Monotonic-2-Diet-wythoff-game.pddl") #dui
    # domain = PDDLParser("./pddl/Monotonic-3-Diet-wythoff-game.pddl")
    # domain = PDDLParser("./pddl/Wythoff-Game-with-set-K-limit($K-=-{1}$).pddl")
    # domain = PDDLParser("./pddl/Wythoff-Game-with-set-K-limit($K-=-{2}$).pddl")
    # domain = PDDLParser("./pddl/Wythoff-v1-4.pddl")
    # domain = PDDLParser("./pddl/Wythoff-v1-1.pddl") #dui
    domain = PDDLParser("./pddl/Wythoff-v1-3.pddl")

    gen = MisereGenerator(domain)
    formula_template = gen.generate_formula(0,0)
    formula = simplify(formula_template.formula_model())
    cost1 = time.time() - start
    print('*' * 50)
    print('N-formula:\n\t %s' % formula)

    strategies = gen.generate_strategy()
    cost2 = time.time() - start
    print('*' * 50)
    print('strategies:\n', strategies)

    if not os.path.exists("./log"):
        os.mkdir("./log")
    with open("./log/%s" % domain.name, "a") as f:
        print("\n*******************Finished*******************")
        print('N-formula:\n\t %s' % formula)
        print('time cost:\n\t %s' % cost1)
        print('strategies:\n\t %s' % strategies)
        print('time cost:\n\t %s' % cost2)

        print('\nmisere rule', file=f)
        print('N-formula:\t %s' % formula, file=f)
        print('time cost:\t %s' % cost1, file=f)
        print('strategies:\t %s' % strategies, file=f)
        print('time cost:\t %s' % cost2, file=f)
