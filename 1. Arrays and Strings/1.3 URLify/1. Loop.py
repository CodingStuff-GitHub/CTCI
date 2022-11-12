# First count the spaces
# Triple it and add those spaces in the last of the string
# Starting from end of string copy the character and put it
# Cannot do that in python because it's string are not immutable
# Can do in JAVA, because of stringbuilder
def urlify(input_string):
    i = 0
    # Pretty Similar to directly using str.replace
    while i < len(input_string):
        if input_string[i] == ' ':
            # just replace when find space
            input_string = f"{input_string[:i]}%20{input_string[i+1:]}"
        i += 1
    return input_string


print(urlify("Mr John Smith"))
