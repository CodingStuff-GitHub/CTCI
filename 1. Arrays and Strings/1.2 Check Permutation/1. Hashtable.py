# O(n)  - Hashtable
# Traverse the first string and put it in the hash table
# Second string will be traversed and checked if it is in hash table
def check_permutation(input_string_1, input_string_2):
    # f is for difference. since 'a' starts from 97 we will subtract 97 so that it starts from 0
    f = ord('a')
    # hash table for 26 characters
    hashmap = [0 for _ in range(ord('a'), ord('z') + 1)]
    # Loop through each character and increment it in hash table (remember to count frequencies)
    for i in input_string_1:
        index = ord(i) - f
        hashmap[index] += 1
    # Loop through each character and check if it is in hash table but after subtracting one frequency
    for j in input_string_2:
        index = ord(j) - f
        hashmap[index] -= 1
        if hashmap[index] < 0:
            return False
    return True


print(check_permutation("abcd", "acdb"))
print(check_permutation("abcde", "afcdb"))
print(check_permutation("aacc", "ccac"))
