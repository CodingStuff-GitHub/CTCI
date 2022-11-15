# StringBuilder should be used
def string_compression(input_string):
    # current is the current element that is being counted
    curr = input_string[0]
    # Frequency of the current element
    count = 0
    # Adding it to the final_string that will be returned
    final_string = ""
    for i in input_string:
        # If the current element is not equal to the element that means that current element count is over
        if i != curr:
            # Adding the current element to the final_string and its count as well
            final_string += str(curr) + str(count)
            # Chaning current element to the i
            curr = i
            # Count is not equal to zero because the current element will be counted as 1 then next element will be 2
            count = 1
        else:
            # Just increment count when the current element and i are equal
            count += 1
    # One last element will be remaining because there was no element after that to stop it
    final_string += str(curr) + str(count)
    # We will return the final string but only if its length is smaller than the input string length or
    # else we will return the input string because maybe every element was unique
    return final_string if len(final_string) < len(input_string) else input_string


print(string_compression("aabcccccaaa"))
