def first_non_repeated_char(s):
    # create a dictionary to keep track of character counts
    char_count = {}
    # loop through the string and count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # loop through the string again and return the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    # if there are no non-repeated characters, return None
    return None
s = "hello world"
print(first_non_repeated_char(s))  # prints 'h'

s = "abracadabra"
print(first_non_repeated_char(s))  # prints 'b'
