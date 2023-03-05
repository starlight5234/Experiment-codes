Input_Source = open("macro.asm", "r",encoding="utf-8")

Macro_Stack = []
MNT = {}
ALA = []
MDT = []

def MacroPass1():
    macro_just_begin = 0
    macro_began = 0
    n = 0
    macro_name = ''
    loc = 0

    for lines in Input_Source.readlines():
        args_list = lines.replace(',','').split()

        for x in args_list:
            if x in MNT.keys():
                args_list.pop(args_list.index(x))
                ALA.append({x:args_list})

        if 'macro' in lines.lower():
            n += 1
            macro_just_begin = 1
            Macro_Stack.append(n)
            continue

        if macro_began or macro_just_begin:
            loc += 1
            MDT.append([loc, lines.strip()])   

        if macro_just_begin:
            macro_def_list = lines.replace(',','').split()
            for args in macro_def_list:
                if '&' not in args:
                    macro_name = args
                    MNT.update({macro_name:loc})
                    macro_began = 1
                    continue

            macro_def_list.pop(macro_def_list.index(macro_name))
            macro_just_begin = 0
            continue        

        if macro_began and not macro_just_begin:
            macro_def_list = lines.replace(',',' ').split()
            for args in macro_def_list:
                if 'mend' in args.lower():
                    Macro_Stack.pop()
                    macro_began = 0
                    macro_name = ''
            continue
    
        if lines.strip().lower() == 'end':
            if len(Macro_Stack) != 0:
                print("Missing a 'MEND'")
                raise SystemExit

        
def printMacroProcData():
    print('---- MNT ----')
    print('Name\tMDT index')
    for macro, loc in MNT.items():
        print('{}\t{}'.format(macro, loc))

    print('')
    print('---- ALA ----')
    for names in ALA:
        i = 0
        for macro, args in names.items():
            print('ALA for {}'.format(macro))
            print('Index\tArgument')
            for x in args:
                print('{}\t{}'.format(i,x))
                i += 1
            print('')

    print('---- MDT ----')
    print('LOC\tMacro Content')
    for lines in MDT:
        print('{}\t{}'.format(lines[0], lines[1]))

import sys
original_stdout = sys.stdout
with open('macro_pass1_output.txt', 'w') as f:
    sys.stdout = f
    MacroPass1()
    printMacroProcData()
sys.stdout = original_stdout
