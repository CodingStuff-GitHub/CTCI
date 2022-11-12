# O(n log n) - No additional data structures required
def is_unique(input_str):
    # Sort the Input string
    input_str = ''.join(sorted(input_str))
    # Loop through the string start from 1st character (Not from zero because we are subtracting 1 from the index)
    for i in range(1, len(input_str)):
        # Check if previous character is same as current character
        if input_str[i] == input_str[i - 1]:
            return False
    return True


print(is_unique("abcd"))
print(is_unique("abcdea"))
