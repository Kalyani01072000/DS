def find_pairs(arr, target_sum):
    pairs = []
    # create an empty set to keep track of seen numbers
    seen = set()
    # loop through the array
    for num in arr:
        # calculate the difference between the target sum and the current number
        diff = target_sum - num
        # if the difference is in the seen set, we have a pair
        if diff in seen:
            pairs.append((diff, num))
        # add the current number to the seen set
        seen.add(num)
    return pairs
arr = [2, 4, 6, 8, 10]
target_sum = 12
pairs = find_pairs(arr, target_sum)
print(pairs)  # prints [(2, 10), (4, 8)]
