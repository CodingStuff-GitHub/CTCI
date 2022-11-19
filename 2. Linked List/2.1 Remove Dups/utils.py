class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(arr):
    head = Node(arr[0], None)
    point = head
    for i in range(1, len(arr)):
        temp = Node(arr[i], None)
        point.next = temp
        point = point.next
    return head


def print_list(ll):
    arr = []
    while ll is not None:
        arr.append(ll.val)
        ll = ll.next
    print(" -> ".join([str(i) for i in arr]))
    return arr
