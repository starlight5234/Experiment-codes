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
PoolTable = [0]

loc_counter = 0
started = False
literal_counter = 0
literal_idx = 0

def instruction_code(loc_counter:int ,instructions:str, *args):
    global literal_idx

    instructions_list = instructions.split(',')
    pair = str("("+ instructions_list[0] + "," + instructions_list[1]+")")
    if len(args) != int(instructions_list[2]) and instructions != MOT["LTORG"]:
        print("{}\t ArguementError, expected {} got {}".format(loc_counter, instructions_list[2], len(args)))
        exit()
    if loc_counter == 0:
        print("\t", pair, "\t" , end='')
    else:
        print(loc_counter, "\t" , pair, "\t" , end='')

    for x in args:
        # print(x, end='')
        if instructions == MOT["LTORG"]:
            z = x.strip("=F'")
            print(' (DL,02)(C,{})'.format(z), end='')
        elif str(x).isdigit() == True:
            print(' (C,{})'.format(x), end='')
        elif str(x).__contains__("REG"):
            reg = ord(x.strip(",REG").lower()) - 96
            print(' (RG,{})'.format(reg), end='')
        elif str(x) in list(SymTable):
            print(' (S,{})'.format(list(SymTable).index(x)), end='')
        elif str(x) in [literals[0] for literals in LiteralTable]:
            literal_idx += 1
            print(' (L,{})'.format(literal_idx), end='')

    print('')

def pass1(lines_tuple:tuple):
    global loc_counter, started, literal_counter

    # print(f'{started} | {loc_counter}: {lines_tuple}')

    # START and END check
    if lines_tuple[0].lower() in AD.keys():
        if started == False:
            if lines_tuple[0].lower() == "start":
                started = True # Pass 1 has begun
                instruction_code(loc_counter, AD["start"], lines_tuple[1])
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
                instruction_code(loc_counter, AD["end"])
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
        instruction_code(loc_counter, MOT[lines_tuple[1]],lines_tuple[2])
        if lines_tuple[1].lower() == "dc":
            SymTable.update({lines_tuple[0]:loc_counter})
            # SymTable.update({lines_tuple[0]:lines_tuple[2]})

        if lines_tuple[1].lower() == "ds":
            SymTable.update({lines_tuple[0]:loc_counter})
            # SymTable.update({lines_tuple[0]:lines_tuple[2]})
            loc_counter = loc_counter + int(lines_tuple[2]) - 1 # -1 for sanity check
    
    if lines_tuple[0] in MOT.keys():
        # print("Mnemonic:", lines_tuple[0])

        if lines_tuple[0].lower() == "origin":
            instruction_code(loc_counter, MOT["ORIGIN"], lines_tuple[1])
            loc_counter = int(lines_tuple[1])
            return

        if lines_tuple[0].lower() == "ltorg":
            # instruction_code(loc_counter, MOT["LTORG"])
            for literals in LiteralTable:
                # print(literals[0])
                instruction_code(loc_counter, MOT["LTORG"], literals[0])
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
        instruction_code(loc_counter, MOT[lines_tuple[0]], lines_tuple[1], lines_tuple[2])
            

    # Increment Location counter address for next line
    loc_counter += 1

def printSymTable(SymTable: dict):
    print('-------Symbol Table-------')
    print("{:<10} {:<10}".format('Label', 'Value(Address)'))
    for key, value in SymTable.items():
        print("{:<10} {:<10}".format(key, value))
    print('\n')

def printLiteralTable(LiteralTable: list):
    print('------Literal Table------')
    print("{:<10} {:<10}".format('Literal', 'Value(Address)'))
    for literals in LiteralTable:
        print("{:<10} {:<10}".format(literals[0], literals[1]))
    print('\n')

def printPoolTable(PoolTable:list):
    print("Pool Table:", PoolTable)
    # for pools in PoolTable:
    #     print(pools)

def printIntermediateCode(asm_input:__file__):
    lines_tuple = []
    for lines in asm_input.readlines():
        lines_tuple = lines.strip().split(" ")
        pass1(lines_tuple)
    print("")

original_stdout = sys.stdout

with open('Intermediate_Code.txt', 'w') as f:
    sys.stdout = f
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
