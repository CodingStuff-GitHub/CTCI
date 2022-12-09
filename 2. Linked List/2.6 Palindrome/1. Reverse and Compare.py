from utils import create_list, print_list
import copy


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


def compare_list(head, reverse_head):
    while head is not None and reverse_head is not None:
        if head.val != reverse_head.val:
            return False
        head = head.next
        reverse_head = reverse_head.next
    return True


def palindrome_check(head):
    reverse_head = reverse_list(copy.deepcopy(head))
    return compare_list(head, reverse_head)


head = create_list([20, 7, 4, 4, 7, 20])
print_list(head)
print(palindrome_check(head))
