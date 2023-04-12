def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)
    
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)
stack = [1, 2, 3, 4, 5]
print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)
