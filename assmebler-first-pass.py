# Assmebler directives
AD = {"start", "end"}

# Mnemonics OP Table
MOPT = {"mover", "movem", "add", "sub", "mult", "div", "print", "read", "origin", "ltorg", "dc", "ds"}

asm_input = open("dummy.asm", "r", encoding="utf-8")

SymTable = {}
LiteralTable = []

loc_counter = 0
started = False
literal_counter = 0

def pass1(lines_tuple:tuple):
    global loc_counter, started, literal_counter

    # print(f'{started} | {loc_counter}: {lines_tuple}')

    # START and END check
    if lines_tuple[0].lower() in AD:
        if started == False:
            if lines_tuple[0].lower() == "start":
                started = True # Pass 1 has begun
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
                started = False # Pass 1 has ended
                return
    
    # Check if 1st column is a label or mnemonic
    # If it is a label add/update to symbol table
    # If it is a mnemonic check for literals or symbols used
    if lines_tuple[0].lower() not in MOPT and lines_tuple[1].lower() in MOPT:
        # print("Label:", lines_tuple[0])
        # print("Mnemonic:", lines_tuple[1])
        if lines_tuple[1].lower() == "dc":
            SymTable.update({lines_tuple[0]:loc_counter})
            # SymTable.update({lines_tuple[0]:lines_tuple[2]})

        if lines_tuple[1].lower() == "ds":
            SymTable.update({lines_tuple[0]:loc_counter})
            # SymTable.update({lines_tuple[0]:lines_tuple[2]})
            loc_counter = loc_counter + int(lines_tuple[2]) - 1 # -1 for sanity check
    
    if lines_tuple[0].lower() in MOPT:
        # print("Mnemonic:", lines_tuple[0])

        if lines_tuple[0].lower() == "origin":
            loc_counter = int(lines_tuple[1])
            return

        if lines_tuple[0].lower() == "ltorg":
            for literals in LiteralTable:
                literals[1] = loc_counter
                loc_counter += 1

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
            else:
                # print("New Symbol:", lines_tuple[2])
                SymTable.update({lines_tuple[2]:'?'})

    # Increment Location counter address for next line
    loc_counter += 1

def printSymTable(SymTable: dict):
    print("{:<10} {:<10}".format('Label', 'Value(Address)'))
    for key, value in SymTable.items():
        print("{:<10} {:<10}".format(key, value))
    print('')

def printLiteralTable(LiteralTable: list):
    print("{:<10} {:<10}".format('Literal', 'Value(Address)'))
    for literals in LiteralTable:
        print("{:<10} {:<10}".format(literals[0], literals[1]))
    print('')

lines_tuple = []

for lines in asm_input.readlines():
    lines_tuple = lines.strip().split(" ")
    pass1(lines_tuple)
    
printSymTable(SymTable)
printLiteralTable(LiteralTable)