#!/usr/bin/python3

import sys

def input_handler(file):
    matrix = 0
    for line in file:
        if matrix%2 == 0:
            yield (read_input_row(line),"A")
        else:
            yield (read_input_col(line),"B")
        
        matrix += 1

def read_input_row(line):
    return line.split(';')

def read_input_col(line):
    cols = []
    data = line.split(';')

    for i in range(len(data[0].split(' '))):
        try:
            cols.append(" ".join([ j.split(' ')[i] for j in data ]))
        except:
            pass
    
    return cols    

def main(separator='\t'):
    
    data = input_handler(sys.stdin)

    for words,_type in data:

        for index,word in enumerate(words):
            print(f'{index + 1}{_type}{separator}{word}')

if __name__ == "__main__":
    main()
