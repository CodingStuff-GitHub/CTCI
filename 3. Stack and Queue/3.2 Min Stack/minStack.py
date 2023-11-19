stack = []


def push(ele: int) -> None:
    if not stack:
        minimum = ele
    else:
        minimum = peek()[1]
    stack.append(ele, min(minimum, ele))


def pop():
    if not stack:
        raise ValueError("Cannot perform pop on an empty stack.")
    else:
        return stack.pop()[0]


def min():
    if not stack:
        raise ValueError("Cannot perform minimum on an empty stack.")
    else:
        return stack.peek()[1]


def peek():
    return stack[-1]


def isEmpty():
    return not len(stack)
