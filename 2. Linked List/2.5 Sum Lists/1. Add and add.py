from utils import create_list, print_list, append_at_tail


def two_linked_list(first, second):
    # head for new linked list
    head = None
    # carry is carry 0,1
    carry = 0
    # Add while both have elements
    while first is not None and second is not None:
        # Add elements from first and second with carry
        add = first.val + second.val + carry
        # Calculate carry
        carry = add // 10
        # Append last digit of add
        head = append_at_tail(head, add % 10)
        first, second = first.next, second.next

    # Maybe elements left in first add them as well in the new linked list but make sure you are taking account of the carry
    while first is not None:
        add = first.val + carry
        carry = add // 10
        head = append_at_tail(head, add % 10)
        first = first.next

    # Maybe elements left in second add them as well and make sure you are taking account of the carry
    while second is not None:
        add = second.val + carry
        carry = add // 10
        head = append_at_tail(head, add % 10)
        second = second.next

    # Lastly if carry is left, It should be added as well in the new linked list
    if carry > 0:
        head = append_at_tail(head, carry)

    return head


first = create_list([9, 9, 9, 9, 9, 9])
second = create_list([1, 1, 5])
head = two_linked_list(first, second)
print_list(head)
