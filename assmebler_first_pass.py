import sys

# Assmebler directives
# AD = {"start", "end"}
AD = {
    "start": "AD,01,1",
    "end": "AD,02,0"
    }

# Mnemonics OP Table
MOT = { 
    "DC": "DL,02,1",
    "DS": "DL,01,1",
    'ADD': 'IS,01,2',
    'SUB': 'IS,02,2',
    'MUL': 'IS,03,2',
    'MOVER':'IS,04,2',
    'MOVEM':'IS,05,2',
    'READ': 'IS,09,1',
    'PRINT':'IS,10,1',
    'ORIGIN':'AD,03,1',
    'LTORG': 'AD,05,0'
    }

asm_input = open("dummy.asm", "r", encoding="utf-8")

SymTable = {}
LiteralTable = []
PoolTable = []

loc_counter = 0
started = False
literal_counter = 0
literal_idx = 0

def instruction_code(loc_counter:int, isLabel:bool , instructions:str, *args):
    global literal_idx

    instructions_list = instructions.split(',')
    pair = str("("+ instructions_list[0] + "," + instructions_list[1]+")")

    if isLabel and len(args) != int(instructions_list[2])+1:
        print("{}\t ArguementError, expected {} got {}".format(loc_counter, int(instructions_list[2])+1, len(args)))
        exit()

    if len(args) != int(instructions_list[2]) and instructions != MOT["LTORG"] and not isLabel:
        print("{}\t ArguementError, expected {} got {}".format(loc_counter, instructions_list[2], len(args)))
        exit()
    if loc_counter == 0:
        print("\t", pair, "\t" , end='')
    elif isLabel and args[0] in list(SymTable):
        print(loc_counter, "\t" , '(S,{})'.format(list(SymTable).index(args[0])) , '\t' , pair.strip(' '), '\t', end='')
    else:
        print(loc_counter, "\t" , pair, "\t" , end='')

    for x in args:
        # print(x, end='')
        if instructions == MOT["LTORG"]:
            z = x.strip("=F'")
            print(' (DL,02)(C,{})'.format(z), end='\t')
        elif str(x).isdigit() == True:
            print(' (C,{})'.format(x), end='\t')
        elif str(x).__contains__("REG"):
            reg = ord(x.strip(",REG").lower()) - 96
<<<<<<< HEAD
            print(' (RG,{})'.format(reg), end='\t')
        elif str(x) in list(SymTable) and not isLabel:
            print(' (S,{})'.format(list(SymTable).index(x)), end='\t')
        elif str(x) in [literals[0] for literals in LiteralTable]:
            literal_idx += 1
            print(' (L,{})'.format(literal_idx), end='\t')
=======
            print(' (RG,{})'.format(reg), end='')
        elif str(x) in list(SymTable):
            print(' (ST,{})'.format(list(SymTable).index(x)), end='')
        elif str(x) in [literals[0] for literals in LiteralTable]:
            literal_idx += 1
            print(' (LT,{})'.format(literal_idx), end='')
>>>>>>> c4bb8f9 (pass1: Make it clear)

    print('')

def pass1(lines_tuple:tuple):
    global loc_counter, started, literal_counter

    # print(f'{started} | {loc_counter}: {lines_tuple}')

    # START and END check
    if lines_tuple[0].lower() in AD.keys():
        if started == False:
            if lines_tuple[0].lower() == "start":
                started = True # Pass 1 has begun
                instruction_code(loc_counter, False, AD["start"], lines_tuple[1])
                if len(lines_tuple) > 1:
                    loc_counter = int(lines_tuple[1])
                    return
            if lines_tuple[0].lower() == "end":
                print("Invalid code!")
                exit()
        else:
            if lines_tuple[0].lower() == "start":
                print("Invalid code!")
                exit()
            if lines_tuple[0].lower() == "end":
                instruction_code(loc_counter, False, AD["end"])
                for literals in LiteralTable:
                    if literals[1] == '?':
                        literals[1] = loc_counter
                        loc_counter += 1

                started = False # Pass 1 has ended
                return
    
    # Check if 1st column is a label or mnemonic
    # If it is a label add/update to symbol table
    # If it is a mnemonic check for literals or symbols used
    if lines_tuple[0] not in MOT.keys() and lines_tuple[1] in MOT.keys():
        # print("Label:", lines_tuple[0])
        # print("Mnemonic:", lines_tuple[1])
        if lines_tuple[1].lower() == "dc":
            SymTable.update({lines_tuple[0]:loc_counter})
            # SymTable.update({lines_tuple[0]:lines_tuple[2]})

        if lines_tuple[1].lower() == "ds":
            SymTable.update({lines_tuple[0]:loc_counter})
            # SymTable.update({lines_tuple[0]:lines_tuple[2]})
            loc_counter = loc_counter + int(lines_tuple[2]) - 1 # -1 for sanity check

        instruction_code(loc_counter, True, MOT[lines_tuple[1]], lines_tuple[0], lines_tuple[2])
    
    if lines_tuple[0] in MOT.keys():
        # print("Mnemonic:", lines_tuple[0])

        if lines_tuple[0].lower() == "origin":
            instruction_code(loc_counter, False, MOT["ORIGIN"], lines_tuple[1])
            loc_counter = int(lines_tuple[1])
            return

        if lines_tuple[0].lower() == "ltorg":
            # instruction_code(loc_counter, False, MOT["LTORG"])
            for literals in LiteralTable:
                # print(literals[0])
                instruction_code(loc_counter, False, MOT["LTORG"], literals[0])
                literals[1] = loc_counter
                loc_counter += 1

            PoolTable.append(literal_counter)
            literal_counter = 0
            return
        
        if lines_tuple[0].lower() == "read" or lines_tuple[0].lower() == "print":
            if lines_tuple[1] not in SymTable.keys():
                SymTable.update({lines_tuple[1]:'?'})

        if lines_tuple[1].lower().rfind("reg") != -1:
            if lines_tuple[2].lower().rfind("=") != -1:
                literal_counter += 1
                # print("Literal Count:", literal_counter)
                LiteralTable.append([lines_tuple[2], '?'])
            elif lines_tuple[2] not in SymTable.keys():
                # print("New Symbol:", lines_tuple[2])
                SymTable.update({lines_tuple[2]:'?'})

        # print(lines_tuple[2])
        instruction_code(loc_counter, False, MOT[lines_tuple[0]], lines_tuple[1], lines_tuple[2])
            

    # Increment Location counter address for next line
    loc_counter += 1

def printSymTable(SymTable: dict):
    # print('-------Symbol Table-------')
    print("{:<10} {:<10}".format('Label', 'Value(Address)'))
    for key, value in SymTable.items():
        print("{:<10} {:<10}".format(key, value))
    print('\n')

def printLiteralTable(LiteralTable: list):
    # print('------Literal Table------')
    print("{:<10} {:<10}".format('Literal', 'Value(Address)'))
    for literals in LiteralTable:
        print("{:<10} {:<10}".format(literals[0], literals[1]))
    print('\n')

def printPoolTable(PoolTable:list):
    # print("Pool Table:", PoolTable)
    print(PoolTable)
    # for pools in PoolTable:
    #     print(pools)

def printIntermediateCode(asm_input:__file__):
    # print("---Intermediate Code---")
    lines_tuple = []
    for lines in asm_input.readlines():
        lines_tuple = lines.strip().split(" ")
        pass1(lines_tuple)
    print("")

def PassOneImpl():
    original_stdout = sys.stdout

    with open('Intermediate_Code.txt', 'w') as f:
        sys.stdout = f
        PoolTable.append(0)
        printIntermediateCode(asm_input)       

    with open('Symbol_Table.txt', 'w') as f:
        sys.stdout = f
        printSymTable(SymTable)

    with open('Literal_Table.txt', 'w') as f:
        sys.stdout = f
        printLiteralTable(LiteralTable)

    with open('Pool_Table.txt', 'w') as f:
        sys.stdout = f
        printPoolTable(PoolTable)

    sys.stdout = original_stdout

PassOneImpl()
