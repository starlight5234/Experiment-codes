import re

# Define the grammar using regular expressions
grammar = [
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUMBER", r"\d+(\.\d+)?"),
    ("OPERATOR", r"[\+\-\*/]"),
    ("LEFT_PAREN", r"\("),
    ("RIGHT_PAREN", r"\)"),
    ("ASSIGNMENT", r"\="),
]

# Define the function to perform lexical analysis
def lex(input_string):
    tokens = []
    while input_string:
        match = None
        for token_type, pattern in grammar:
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                input_string = input_string[len(value):].lstrip()
                break
        if not match:
            raise ValueError(f"Invalid input: {input_string}")
    return tokens

# Test the function with an example input string
input_string = input('Input String: ')
tokens = lex(input_string)
print(tokens)