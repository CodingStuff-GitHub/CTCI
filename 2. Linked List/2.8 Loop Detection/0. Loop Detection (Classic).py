from utils import create_list, print_list


def add_loop_to_list(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    return head


def loop_detection(head):
    # Run both slow and fast runner if they collide then its a looped linked list if not then one of them will reach the end
    fast = slow = head
    while fast is not None and slow is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return "Loop Detected"
    return "Loop not Detected"


head = create_list([20, 7, 6, 3, 5, 9])
print_list(head)

print(loop_detection(head))
head = add_loop_to_list(head)
print(loop_detection(head))
