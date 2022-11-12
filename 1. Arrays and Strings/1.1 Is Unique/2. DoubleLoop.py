# O(n^2) - No additional data structures required
def is_unique(input_str):
    # First loop to take single element
    for i in range(len(input_str)):
        # Second loop to check with next all elements in the string
        for j in range(i + 1, len(input_str)):
            # If found a duplicate element return False
            if input_str[i] == input_str[j]:
                return False
    # No duplicate elements found return True
    return True


print(is_unique("abcd"))
print(is_unique("abcda"))
