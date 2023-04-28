import exp7

exp = input("Enter your expression: ")
pos = exp7.infix_to_postfix(exp)
res = exp7.generate3AC(pos)

op_code = {
    '+' : 'ADD',
    '-' : 'SUB',
    '*' : 'MUL',
    '/' : 'DIV'
}

reg = {}

def CodeGen(res):
    reg_idx = 1
    moved = {}
    curr_reg = {}

    for exps in res:
        print(f'\n#{exps[0]} = {exps[1]} {exps[2]} {exps[3]}')
        operands = [1,3]
        new = []

        for x in operands:
            if exps[x] not in moved and '#' not in exps[x]:
                moved.update({exps[x]: reg_idx})
                reg_idx += 1
                new.append(exps[x])
            if exps[x] not in moved and '#' in exps[x]:
                moved.update({ '#' + str(exps[x]).strip('#'): curr_reg[int(str(exps[x]).strip('#'))]})

        for x in new:
            print(f'MOV R{moved[x]}, {x}')

        print(f'{op_code[exps[2]]} R{moved[exps[1]]}, R{moved[exps[3]]}')
        curr_reg.update({exps[0]: moved[exps[1]]})
        
CodeGen(res)