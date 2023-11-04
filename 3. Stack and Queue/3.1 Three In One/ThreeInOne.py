# Three Stack in Single Array
arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# Top
tops = [-1, -1, -1]


def push(stack_number: int, element: int) -> int:
    if arr[-1] != -1:
        print("Full stack. Cannot insert.")
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
    return 0


def pop(stack_number: int) -> int:
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


def is_empty(stack_number: int) -> bool:
    return tops[stack_number] in [-1, tops[stack_number - 1]]
