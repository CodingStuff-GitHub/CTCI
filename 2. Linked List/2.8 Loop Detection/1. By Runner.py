# Look for Flyod's Cycle Detection
# When the slow pointer and fast pointer move together, then the slow pointer reaches the beginning
# of the loop then the fast pointer reaches the 'k' steps ahead
# Now if we wait for them to collide, then put the slow pointer at head of the list and then advance both pointers one by one
# When they will collide again, that will be the beginning of the loop

from utils import create_list, print_list, append_at_head


def add_loop_to_list(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    return head


def loop_detection(head):
    if head is None or head.next is None:
        return None
    # Run both slow and fast runner till they collide
    slow = fast = head
    while slow is not None and fast is not None:
        slow = slow.next
        if fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
        else:
            return None
        # Dont put it on the while condition because it should run atleast 1
        if slow == fast:
            break

    # Check if previous loop broke because of None condition
    if slow is not None and fast is not None:
        # Get back to head
        slow = head
        # one step at a time
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return "No loop"


head = create_list([20, 7, 6, 3, 5, 9])
print_list(head)

print(loop_detection(head))
head = add_loop_to_list(head)
head = append_at_head(head, 6)
head = append_at_head(head, 10)
head = append_at_head(head, 16)
print_list(head)
print(loop_detection(head), head.val)
