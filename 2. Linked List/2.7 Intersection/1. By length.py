from utils import create_list, print_list


def intersect_at_n(head1, head2, where):
    temp1, temp2 = head1, head2
    i = 0
    while i < where and temp1 is not None:
        i += 1
        temp1 = temp1.next
    while temp2.next is not None:
        temp2 = temp2.next
    temp2.next = temp1
    return head1, head2


def find_intersection(head1, head2):
    # Check if they are actually intersecting - got to last element and check if they are same for both heads
    temp1, temp2 = head1, head2
    length_of_head1 = length_of_head2 = 0
    # Go to last element
    while temp1.next is not None:
        length_of_head1 += 1
        temp1 = temp1.next
    while temp2.next is not None:
        length_of_head2 += 1
        temp2 = temp2.next
    # Check last elements
    if temp1 != temp2:
        # Not intersecting
        return -1
    # Increase the head of the list whose length is longer if neccessary
    diff = abs(length_of_head1 - length_of_head2)
    temp = head1 if length_of_head1 > length_of_head2 else head2
    while diff > 0:
        temp = temp.next
        diff -= 1
    if length_of_head1 > length_of_head2:
        head1 = temp
    else:
        head2 = temp
    # Start both and check if node is same or not
    while head1 is not None and head2 is not None:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return -1


head1, head2 = intersect_at_n(
    create_list([5, 6, 7, 11, 23, 25]),
    create_list([9, 2, 1, 12, 52]),
    3)
print_list(head1)
print_list(head2)
result = find_intersection(head1, head2)
print(result, result.val if result != -1 else "Not Intersecting")
