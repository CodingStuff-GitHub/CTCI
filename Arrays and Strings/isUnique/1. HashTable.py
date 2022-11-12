# Hash Table  - O(n)
def is_unique(input_str):
    # This will help to create the difference when checking in the hash table
    f = ord('a')
    # It will contain key value of the elements that are coming in the nums
    hashmap = [0 for _ in range(ord('a'), ord('z') + 1)]
    # Looping through the array
    for i in input_str:
        key = ord(i) - f
        # If hashmap contains the i key  =  1 then it is not unique i.e it already came before
        if hashmap[key] == 1:
            return False
        else:
            # Not in hashmap means it is unique thus add it to hashmap
            hashmap[key] = 1
    # All unique hashes so return True
    return True


print(is_unique("abcad"))
