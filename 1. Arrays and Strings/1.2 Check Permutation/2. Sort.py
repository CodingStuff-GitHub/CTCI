# Sort the strings and then compare
def check_permutation(input_string_1, input_string_2):
    # Sort the strings
    input_string_1 = ''.join(sorted(input_string_1))
    input_string_2 = ''.join(sorted(input_string_2))
    # Compare the elements of both strings and return false if they are difference
    for i in range(0, len(input_string_1)):
        if input_string_1[i] != input_string_2[i]:
            return False
    return True
