# Copy the next node in the cureent node and next will be next's next
from utils import create_list, print_list


def copy_next_node(middleNode):
    if middleNode.next is not None:
        # Next Value should be put in the current node
        middleNode.val = middleNode.next.val
        # Curret Node next will point to next Node's next
        middleNode.next = middleNode.next.next


head = create_list([1, 3, 4, 5, 6, 7, 9, 11, 98])
# Lets say we want to delete 5
middleNode = head.next.next.next.next
print_list(head)
# middleNode is passed not the head of the list
copy_next_node(middleNode)
print_list(head)
