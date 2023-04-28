import sys, os.path

file_prefix = ['Intermediate_Code', 'Symbol_Table', 'Literal_Table', 'Pool_Table']
asm_input = open("dummy.asm", "r", encoding="utf-8")

for x in file_prefix:
    file_name = '.'.join([x,'txt'])
    if not os.path.isfile(file_name):
        print('Missing {}'.format(file_name.strip('.txt').replace('_',' ')))

intermediate_code = open("Intermediate_Code.txt", "r", encoding="utf-8")
SymTableFile = open("Symbol_Table.txt", "r", encoding="utf-8")
LiteralTableFile = open("Literal_Table.txt", "r", encoding="utf-8")

S = []
dummy_list = iter(list(SymTableFile.read().strip().split()))
for x in dummy_list:
    if not str(x).isdigit():
        S.append([x, next(dummy_list)])
# print(S)

L = []
dummy_list = iter(list(LiteralTableFile.read().strip().split()))
for x in dummy_list:
    if not str(x).isdigit():
        L.append([x.strip(".='"), next(dummy_list)])
# print(L)
# print('\n\n')

literal_counter = 0

# print(intermediate_code.read())
def pass2(lines_tuple:list):
    # Ignore empty tuples
    if len(lines_tuple) == 0:
        return

    machine_code = []

    # print(lines_tuple)
    for x in lines_tuple:
        if str(x).isdigit():
            continue
        
        # print(x)
        instruction = x.strip('()').split(',')
        if instruction[0] == 'IS':
            # print(instruction[1])
            machine_code.append(instruction[1])
        if instruction[0] == 'RG':
            machine_code.append(instruction[1])
        if instruction[0] == 'L':
            # print(L[int(instruction[1])-1])
            machine_code.append(L[int(instruction[1])-1][1])
        if instruction[0] == 'S':
            # print(S[int(instruction[1])][1])
            machine_code.append(S[int(instruction[1])][1])

    if len(machine_code) > 0: 
        print('(', end='')
        print(*machine_code, sep=") (", end='')
        print(')')

def PassTwoImpl():
    lines_tuple = []
    for lines in intermediate_code.readlines():
        lines_tuple = lines.strip().split()
        pass2(lines_tuple)
    print("")

PassTwoImpl()