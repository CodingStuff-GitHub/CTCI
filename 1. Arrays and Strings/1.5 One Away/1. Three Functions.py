# First compare lengths of the first and second and define if operation was removing, inserting, or editing(or no change).
# Then use appropriate function to determine if it was only one operation
# Only one function? Yes, You can make three functions but you will look closely they are pretty much same. Little bit of here and there
# You can combine all the three functions into a single function

def one_way(first, second):
    # If length of first and second differs more than one, then just return False
    if abs(len(first) - len(second)) <= 1:
        return operation_check(first, second)
    return False


def operation_check(first, second):
    # Two pointers for first and second
    p = 0
    q = 0
    # One operation which will be removed whenever we encounter the first operation
    operation = 1

    while p < len(first) and q < len(second):
        # If we dont have any operation and still p and q are not equal, that means first and second differs more than one
        if operation <= 0 and first[p] != second[q]:
            return False
            # First time encounter the "result of operation", minus one from operation and then check for which operation is performed
        elif first[p] != second[q]:
            operation -= 1
            # Which operation was performed? length is greater? Insertion
            if len(first) > len(second):
                q -= 1
            # length is smaller? Deletion
            elif len(first) < len(second):
                q += 1
            # No change of q pointer for edit operation
        q += 1
        p += 1
    return True


print(one_way("pale", "ple"))
print(one_way("pales", "pale"))
print(one_way("pale", "bale"))
print(one_way("pale", "bake"))
print(one_way("hake", "hakse"))
