# Recursively call till we hit None then when coming back count. When k is equal to the count you will get the result
from utils import create_list, print_list


def return_kth_to_last(head, k):
    if head is not None:
        k = return_kth_to_last(head.next, k) - 1
    if k == 0:
        print(head.val)
    return k


head = create_list([1, 3, 4, 5, 6, 7, 9, 11, 98])
print_list(head)
return_kth_to_last(head, 4)
