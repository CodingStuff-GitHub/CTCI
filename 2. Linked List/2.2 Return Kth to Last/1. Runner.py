# Two pointers difference of k. When last pointer will reach at the end then the other pointer will be at kth position
from utils import create_list, print_list


def return_kth_to_last(head, k):
    p1 = head
    p2 = None
    while k and p1 is not None:
        p1 = p1.next
        k -= 1
    if k > 0:
        return "k is greater than number of nodes"
    p2 = head
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2.val


head = create_list([1, 3, 4, 5, 6, 7, 9, 11, 98])
print_list(head)
kth = return_kth_to_last(head, 4)
print(kth)
