# Three Stack in Single Array
arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# Top
tops = [-1, -1, -1]


def push(stackNumber, element):
    if arr[-1] != -1:
        return -1
    # This will be its index position
    position = tops[stackNumber] + 1
    # Insert the value in this position
    i = tops[-1] + 1
    while i > position:
        arr[i] = arr[i - 1]
        i -= 1
    arr[position] = element
    # Updating tops
    for i in range(stackNumber, len(tops)):
        tops[i] += 1
    print(arr)
    print(tops)


push(0, 3)
push(0, 2)
push(2, 5)
push(1, 8)
push(1, 9)
push(2, 1)
push(0, 7)
push(0, 11)
