﻿def do_parentheses_match(input_string):
    s = []
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0


bracket_string = input()
if(do_parentheses_match(bracket_string)):
    print('сбалансированы')
else:
    print('не сбалансированы')
