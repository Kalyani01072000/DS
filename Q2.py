def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # swap the elements at the left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # move the left index to the right
        left += 1
        # move the right index to the left
        right -= 1
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # prints [5, 4, 3, 2, 1]
