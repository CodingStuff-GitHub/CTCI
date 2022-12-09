from utils import create_list, print_list


# Take 2 head and tail infront of the list then add to head is smaller than pivot
# And in tail if greater than pivot
def two_linked_list(head, pivot):
    # New head and tail for the new linked list and next node is for the original linked list tracking
    new_head, new_tail, next_node = head, head, head
    while next_node != None:
        # Making sure we dont lose the next node in original list
        next_node = head.next
        # If smaller than pivot then add it to the head of the linked list
        # If larger than pivot then add it to the tail of the linked list
        if head.val < pivot:
            head.next = new_head
            new_head = head
        else:
            new_tail.next = head
            new_tail = new_tail.next
        # Next head will be the next node in the original linked list
        head = next_node
    return new_head


head = create_list([10, 3, 5, 6, 8, 10, 1, 2, 12, 5, 3, 8])
print_list(head)
head = two_linked_list(head, 5)
print_list(head)
