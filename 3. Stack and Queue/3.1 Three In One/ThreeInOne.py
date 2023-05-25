# Three Stack in Single Array
arr = [-1, -1, -1, -1, -1, -1, -1]

# Every stack has [Base, Top]
stacks = [[-1, -1], [-1, -1], [-1, -1]]


def push(stackNumber, element):
    # No space is there
    if arr[-1] > -1:
        print("No space")
        return -1

    # This stack is empty
    if stacks[stackNumber][0] == -1:
        for i, num in enumerate(arr):
            # Position the new stack in empty place
            if num == -1:
                stacks[stackNumber][0] = stacks[stackNumber][1] = i
                arr[i] = element
                break

    # Stack is not empty
    else:
        # Move all elements after top of this stack by 1
        for i in range(len(arr) - 1, stacks[stackNumber][1], -1):
            arr[i] = arr[i - 1]

        # Increase stack's top and add element to the top
        stacks[stackNumber][1] += 1
        arr[stacks[stackNumber][1]] = element

        # Increase the base and the top of the stacks whose base comes after this stack
        # Because those were the stacks which got shifted by 1
        for i in range(len(stacks)):
            if stacks[i][0] > stacks[stackNumber][0]:
                stacks[i][0] += 1
                stacks[i][1] += 1
    print(stacks)
    print(arr)


def pop(stackNumber):
    if isEmpty(stackNumber) == -1:
        return -1

    # Pick the element
    element = arr[stacks[stackNumber][1]]
    # Move all elements after top of this stack by -1
    for i in range(stacks[stackNumber][1], len(arr)):
        arr[i] = arr[i + 1]

    # decrease top by 1
    stacks[stackNumber][1] -= 1
    # If top is less than the base that means this was the last element to pop and now this stack is empty
    if stacks[stackNumber][1] < stacks[stackNumber][0]:
        stacks[stackNumber] = [-1, -1]

    # Decrease the base and the top of the stacks whose base comes after this stack
    # Because those were the stacks which got shifted by -1
    for i in range(len(stacks)):
        if stacks[i][0] > stacks[stackNumber][0]:
            stacks[i][0] -= 1
            stacks[i][1] -= 1

    print(stacks)
    print(arr)
    return element


def peek(stackNumber):
    return arr[stacks[stackNumber][1]]


def isEmpty(stackNumber):
    if stacks[stackNumber][0] != -1:
        return 1
    print("Nothing in stack")
    return -1


push(0, 3)
push(0, 2)
push(2, 5)
pop(0)
push(1, 8)
push(1, 9)
push(2, 1)
push(0, 7)
push(0, 11)
