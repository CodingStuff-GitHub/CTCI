# First count the spaces
# Triple it and add those spaces in the last of the string
# Starting from end of string copy the character and put it
# Just assuming array of string

def urlify(input_string):
    input_string = list(input_string)

    # 1. Count the spaces
    spaces = input_string.count(' ')
    print(spaces)
    # 2. Add buffer to end of string
    last_char_i = len(input_string) - 1
    # Here we add new spaces at last... (Multiplying with 3 units should be the case because %20 contains 3 characters
    # but the orignal spaces are also taking 1 unit space which will not be necessary when we will add %20.
    # Thats why multiply with 2 will work )
    input_string += '1' * 2 * spaces

    # Take the index at last of the sting
    index = len(input_string) - 1
    # Loop till the original string index is at the beginning
    while last_char_i >= 0:
        print(''.join(input_string), index, last_char_i)
        # If space is present, change it with %20
        if input_string[last_char_i] == " ":
            # Strings are immuatable in Python so doing it on list
            input_string[index] = "0"
            input_string[index - 1] = "2"
            input_string[index - 2] = "%"
            # Go back 3 indices
            index -= 3
        else:
            # Normal character should be kept as it is in the string
            input_string[index] = input_string[last_char_i]
            index -= 1
        last_char_i -= 1
    return ''.join(input_string)


print(urlify("Mr John Smith"))
