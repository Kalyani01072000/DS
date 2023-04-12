def postfix_to_prefix(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for c in postfix:
        if c not in operators:
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(c + op2 + op1)
    return stack.pop()
postfix = "ab*cd/-"
prefix = postfix_to_prefix(postfix)
print(f"Postfix expression: {postfix}")
print(f"Prefix expression: {prefix}")


