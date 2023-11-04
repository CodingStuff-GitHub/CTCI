""" ThreeInOne """
# Three Stack in Single Array
arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# Top
tops = [-1, -1, -1]


def push(stack_number: int, element: int) -> int:
    if arr[-1] != -1:
        print("Full stack")
        return -1
    # This will be its index position
    position = tops[stack_number] + 1
    # Insert the value in this position
    i = tops[-1] + 1
    while i > position:
        arr[i] = arr[i - 1]
        i -= 1
    arr[position] = element
    # Updating tops
    for i in range(stack_number, len(tops)):
        tops[i] += 1
    print(arr)
    print(tops)


def pop(stack_number: int):
    if tops[stack_number] in [-1, tops[stack_number - 1]]:
        print("Empty Stack")
        return -1
    # Remove elements from this to end
    i = tops[stack_number]
    res = arr[tops[stack_number]]
    while i < tops[-1]:
        arr[i] = arr[i + 1]
        i += 1
    arr[i] = -1
    # Updating tops
    for i in range(stack_number, len(tops)):
        tops[i] -= 1
    print(arr)
    print(tops)
    return res


def peek(stack_number: int) -> int:
    return (
        arr[tops[stack_number]]
        if tops[stack_number] not in [-1, tops[stack_number - 1]]
        else -1
    )


print(pop(0))
push(0, 3)
push(0, 2)
push(2, 5)
push(1, 8)
push(1, 9)
push(2, 1)
push(0, 7)
push(0, 11)
print(pop(2))
print(pop(2))
print(pop(2))
print(pop(0))
print(peek(0), peek(1), peek(2))
