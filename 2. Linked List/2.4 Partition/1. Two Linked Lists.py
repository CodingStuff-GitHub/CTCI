from utils import create_list, print_list, append_at_tail


# Two new Linked List which will take smaller and greater(or equal) elements
# then we will merge them together by adding last element next to head of second linked list
def two_linked_list(head, pivot):
    # h1 is for greater(or equal) elements
    # h2 is for less elements
    h1, h2 = None, None
    while head is not None:
        if head.val >= pivot:
            h1 = append_at_tail(h1, head.val)
        else:
            h2 = append_at_tail(h2, head.val)
        head = head.next
    # Going through h2 linked list to get to the last element
    head = h2
    while head.next is not None:
        head = head.next
    # Last element next connects to h1 linked list head
    head.next = h1
    return h2


head = create_list([3, 5, 6, 8, 10, 1, 2, 12, 5, 3, 8])
print_list(head)
head = two_linked_list(head, 5)
print_list(head)
