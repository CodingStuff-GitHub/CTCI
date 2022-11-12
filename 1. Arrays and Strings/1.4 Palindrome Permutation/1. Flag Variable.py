# A flag variable will be used to indicate whether every element came twice and one exta element exist if it is odd length
# This flag will get incremented when hashmap doesnot have the element and decremented when hashmap has the element
# If it is 1 or 0, then the string can become palindrome
def palindrome_permutation(input_string):
    flag = 0
    hashmap = [0 for _ in range(ord('a'), ord('z') + 1)]
    f = ord('a')

    # We will loop through the input string and check if the element came in twice
    for i in range(len(input_string)):
        # Just for spaces, we can check if the element is inside a range by knowing the unicode but for now let it be
        if input_string[i] != ' ':
            # To make the difference correct and get index near zero
            index = ord(input_string[i]) - f
            # if already in hashmap, then it came twice hence can be used in making palindrome
            if hashmap[index] == 1:
                flag -= 1
            else:
                # If not then better add it to hashmap and increase the flag
                hashmap[index] = 1
                flag += 1
    # Flag should be zero or one for even and odd length respectively
    return flag in [0, 1]


print(palindrome_permutation("tact coa"))
