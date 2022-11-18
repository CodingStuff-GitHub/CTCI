# Like HashTable I guess
from utils import create_list, print_list


def remove_dups(head):
    temp = head
    prev = None
    hashset = set()
    while temp is not None:
        if temp.val not in hashset:
            hashset.add(temp.val)
            prev = temp
        else:
            prev.next = temp.next
        temp = temp.next
    return head


head = create_list([1, 3, 4, 3, 5, 6, 7, 3, 1, 6, 8, 5])
print_list(head)
remove_dups(head)
print_list(head)
