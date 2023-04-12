def prefix_to_infix(prefix):
    stack = []
    for i in range(len(prefix)-1, -1, -1):
        if prefix[i].isalnum():
            stack.append(prefix[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1}{prefix[i]}{op2})")
    return stack.pop()
prefix = "-*ab/cd"
infix = prefix_to_infix(prefix)
print(f"Prefix expression: {prefix}")
print(f"Infix expression: {infix}")



