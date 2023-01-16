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


def append_at_tail(head, val):
    if head is None:
        head = Node(val, None)
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(val, None)
    return head


def print_list(ll):
    arr = []
    while ll is not None:
        arr.append(ll.val)
        ll = ll.next
    print(" -> ".join([str(i) for i in arr]))
    return arr


def reverse_list(rev_head):
    curr, prev = rev_head, None
    while curr.next is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    rev_head = curr
    rev_head.next = prev
    return rev_head
