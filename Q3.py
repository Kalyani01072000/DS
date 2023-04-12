def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False
str1 = "hello"
str2 = "lohel"
print(is_rotation(str1, str2))  # prints True

str1 = "abcde"
str2 = "edcba"
print(is_rotation(str1, str2))  # prints False
