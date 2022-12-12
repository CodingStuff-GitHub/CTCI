from utils import create_list, print_list, append_at_tail


def sum_linked_list(first, second, third, carry):
    # value is equal to carry. It can be 1 or 0
    value = carry
    # If node in first exists then add it to value
    if first is not None:
        value += first.val
        first = first.next
    # If node in second exists then add it to value
    if second is not None:
        value += second.val
        second = second.next
    # append_at_tail in third
    third = append_at_tail(third, value % 10)
    # Calucate the new carry
    carry = value // 10
    # If something is pending
    if first is not None or second is not None or carry > 0:
        # Call the function recursively with the appropriate parameters
        sum_linked_list(
            first if first is not None else None,
            second if second is not None else None,
            third, carry)
    # It is just for the first call from function
    return third


first = create_list([9, 9, 9, 9, 9, 9])
second = create_list([1, 1, 5])
head = sum_linked_list(first, second, None, 0)
print_list(head)
