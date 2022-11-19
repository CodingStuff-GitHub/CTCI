# Double pointer just like double loops
# No buffer allocated
from utils import create_list, print_list


def remove_dups(head):
    i = head
    while i is not None:
        prev = i
        j = i.next
        while j is not None:
            if i.val != j.val:
                prev = j
            else:
                prev.next = j.next
            j = j.next
        i = i.next


head = create_list([1, 3, 4, 3, 5, 6, 7, 3, 1, 6, 8, 5])
print_list(head)
remove_dups(head)
print_list(head)
