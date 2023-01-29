from utils import create_list, print_list


def palindrome_check(head):
    slow, fast = head, head.next
    stack = [slow]
    # Loop for runner and put it in stack
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        stack.append(slow)
    # Check for odd if yes do double jump or else single jump
    slow = slow.next.next if fast.next is not None else slow.next
    # 2nd Loop continues ith the slow runner
    while slow is not None:
        if stack.pop().val != slow.val:
            return False
        slow = slow.next
    return True


head = create_list([20, 7, 4, 4, 7, 20])
print_list(head)
print(palindrome_check(head))
head = create_list([20, 7, 4, 4, 7, 20, 1])
print_list(head)
print(palindrome_check(head))
head = create_list([20, 7, 4, 1, 4, 7, 20])
print_list(head)
print(palindrome_check(head))
