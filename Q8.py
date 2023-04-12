def is_balanced(code):
    stack = []
    for char in code:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return False
            open_bracket = stack.pop()
            if open_bracket == '(' and char != ')':
                return False
            elif open_bracket == '{' and char != '}':
                return False
            elif open_bracket == '[' and char != ']':
                return False
    return not stack
code = "(a+b)*(c-d)"
if is_balanced(code):
    print("The code is balanced.")
else:
    print("The code is not balanced.")
