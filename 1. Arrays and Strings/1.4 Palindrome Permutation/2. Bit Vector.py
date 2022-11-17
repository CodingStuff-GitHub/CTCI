# We dont need to count  the number of odds of any character, we can think about it as a switch if it is OFF when started from OFF
# No matter how many times i flipped it will be even only. We will use a bit vector for all 26 characters. When we have to check
# if it already came or not, we will subract from 1 and then AND with the result
# It should give zero if there is a single 1 in the vector
# First XOR the characters with the checking bit vector
# Then subtract the checking bit vector - 1 then and with it
def palindrome_permutation(input_string):
    f = ord('a')
    check = 0  # 0000 0000
    for i in range(len(input_string)):
        index = ord(input_string[i]) - f
        mask = 1 << index  # for c - mask will be ...0000 0100
        check = check ^ mask  # If c is already there it will be zero but if not then it will be 1
    # Til now the check will be zero (It was odd length) or it will have only one bit which will be 1 to return true
    result = check - 1
    # This result will be very opposite to the check. When we will AND with it, it will become zero
    return True if check == 0 else not (check & result)


print(palindrome_permutation("tactcoa"))
