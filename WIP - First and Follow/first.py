productions = {
    'S' : ['ABC', 'CbB', 'Ba'],
    'A' :['da', 'BC'],
    'B' :['g', '#'],
    'C' :['h', '#']
}

firsts = {}
follows = {}

def first(symbol: str, symbol_prod: list):
    global productions, firsts

    if symbol not in firsts.keys():
        firsts.update({symbol:[]})

    for prods in symbol_prod:
        lst = firsts[symbol]

        if prods[0].islower() or prods[0] == '#':
            if prods[0] not in lst:
                lst.append(prods[0])
        
        if prods[0].isupper():
            for x in first(prods[0], productions[prods[0]]):
                if x not in lst:
                    lst.append(x)

                if x == '#':
                    print(prods)

    
    return firsts[symbol]

def follow(symbol: str, symbol_prod: list):
    global productions, follows, firsts

    prod_list_values = list(productions.values())
    prod_list_keys = list(productions.keys())

    temp = []
    temp_follows = []

    for x in productions.values():
        for prods in x:
            if symbol in prods:
                temp.append(prods)

    if symbol not in follows.keys():
        follows.update({symbol:[]})

    if len(temp) == 0:
        temp_follows.append('$')
    else:
        for prods in temp:
            if prods.index(symbol) == len(prods) - 1:
                # Edge case
                for x in prod_list_values:
                    if prods in x:
                        for y in follows[prod_list_keys[prod_list_values.index(x)]]:
                            temp_follows.append(y)

            try:
                # first of symbol or first of next of symbol if epsilon
                idx = prods.index(symbol) + 1
                prods[idx]

                # Symbols
                if prods[idx].islower() == False:
                    # Check if contains epsilon
                    while '#' in firsts[prods[idx]]:
                        lst = firsts[prods[idx]].copy()
                        lst.remove('#')
                        for x in lst:
                            temp_follows.append(x)
                        
                        if idx == len(prods) - 1:
                            # Edge reached
                            for x in prod_list_values:
                                if prods in x:
                                    for y in follows[prod_list_keys[prod_list_values.index(x)]]:
                                        temp_follows.append(y)

                        idx += 1

                # Non-Terminal        
                else:
                    temp_follows.append(prods[idx])
                    
            except IndexError:
                pass

    follows[symbol] = list(set(temp_follows))

    return follows[symbol]

print(f'Prod \t First')
for syms in productions.keys():
    print(f'{syms} \t {first(syms, productions[syms])}')

print()
print(f'Prod \t Follow')
for syms in productions.keys():
    print(f'{syms} \t {follow(syms, productions[syms])}')