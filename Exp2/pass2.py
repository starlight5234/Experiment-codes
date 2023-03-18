import sys

pass2_input = open("Intermediate_Code.txt", "r", encoding="utf-8")
SymT = open("Symbol_Table.txt", "r", encoding="utf-8").read().strip().split('\n')
LiT = open("Literal_Table.txt", "r", encoding="utf-8").read().strip().split('\n')

SymTable = []
for x in SymT:
    # print(x.split())
    SymTable.append(x.split()[1])

LiTable = []
for x in LiT:
    # print(x.split())
    LiTable.append(x.split()[1])

AD_marker = 0
DL_marker = 0

def filtercode(line_list: list, output: dict):
    global AD_marker, DL_marker
    for pair in line_list:

        if 'AD' in pair or AD_marker == 1:
            AD_marker = 1
            if 'DL' in pair or DL_marker == 1:
                DL_marker = 1
                if 'C' in pair:
                    dum = pair.split(',')[2].strip(')')
                    output.update({"LT": format(int(dum), "03d")})
                else:
                    AD_marker = 0
                    DL_marker = 0

        if 'IS' in pair:
            dum = pair.split(',')[1].strip(')')
            output.update({"IS": dum})
        if 'RG' in pair:
            dum = pair.split(',')[1].strip(')')
            output.update({"RG": format(int(dum), "02d")})
        if 'ST' in pair:
            dum = pair.split(',')[1].strip(')')
            output.update({"ST": SymTable[int(dum)]})
        if 'LT' in pair:
            dum = pair.split(',')[1].strip(')')
            output.update({"LT": LiTable[int(dum)-1]})

def printMachineCode(output_current_line: dict):
    if 'IS' in output_current_line.keys():
        print(output_current_line['IS'], end="\t")
    else:
        print('00', end="\t")
    
    if 'RG' in output_current_line.keys():
        print(output_current_line['RG'], end="\t")
    else:
        print('00', end="\t")

    ST_marker = 0

    if 'ST' in output_current_line.keys():
        print(output_current_line['ST'], end="\t")
        ST_marker = 1
    else:
        ST_marker = 0
    
    if ST_marker == 0:
        if 'LT' in output_current_line.keys():
            print(output_current_line['LT'], end="\t")
        else:
            print('00', end="\t")
    
    print('')


def PassTwoImpl():
    original_stdout = sys.stdout

    with open('Machine_Code.txt', 'w') as f:
        sys.stdout = f
        print("Machine Code:")
        print("IS\tRG\tST/LT")

        for lines in pass2_input.readlines():
            output_current_line = {}
            line_list = lines.strip().split()
            if len(line_list) != 0:
                if line_list[0].isnumeric():
                    filtercode(line_list, output_current_line)
            
            if len(output_current_line): 
                printMachineCode(output_current_line)

    sys.stdout = original_stdout

PassTwoImpl()