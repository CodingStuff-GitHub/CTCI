# Save Space by this
def is_unique(input_str):
    check = 0  # 0000 0000

    for i in range(len(input_str)):
        # Find the index by difference between first and the current character
        index = ord(input_str[i]) - ord('a')
        # Bit shift 1 to the character position
        # For Ex - if we encounter 'c', then it will be shifted by 3 (index)
        # and value will become 0000 0100
        value = 1 << index
        # AND between check and value. AND will check if value is unique or not. If 'ç' was already in 'check' then it's bit wil be 1
        # and our value will also have 1 bit on the same place. Thus AND will give 1 as a result and it will be greater than zero
        if check & value > 0:
            return False
        else:
            # If value 'AND' check are giving zero, that means the value was unique and OR will help the value to put in that index.
            check |= value
    return True


print(is_unique("abcfde"))
print(is_unique("abcdfeaf"))
