def find_smallest(stack):
    if not stack:
        return None
    min_val = stack.pop()
    while stack:
        temp = stack.pop()
        if temp < min_val:
            min_val = temp
    return min_val
stack = [3, 5, 1, 4, 2]
print("Stack:", stack)
smallest = find_smallest(stack)
print("Smallest number in stack:", smallest)
