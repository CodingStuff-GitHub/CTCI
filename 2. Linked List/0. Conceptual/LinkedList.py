class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        return " -> ".join(str(i) for i in arr)

    # Create a linked list from an array.
    def create_list(self, arr):
        self.head = Node(arr[0], None)
        temp = self.head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i], None)
            temp = temp.next

    # Append a node at the tail of the linked list.
    def append_at_tail(self, val):
        if self.head is None:
            self.head = Node(val, None)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val, None)

    # Delete the node from the linked list
    def delete_node(self, val):
        if self.head is None:
            print("Linked List is empty")
        # Deleting head of the Linked List
        elif self.head.val == val:
            self.head = self.head.next
        else:
            # Deleting Elsewhere
            temp = self.head
            prev = None
            while temp.val != val and temp.next is not None:
                prev = temp
                temp = temp.next
            if temp is not None and temp.val == val:
                prev.next = temp.next
            else:
                print("Node Not Found")

    # Empty the linked list
    def clear(self):
        self.head = None


head = LinkedList()
head.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
head.append_at_tail(10)
print(head)
# Delete from anywhere
head.delete_node(6)
print(head)
# Delete from start
head.delete_node(1)
print(head)
# Delete from end
head.delete_node(10)
print(head)
# Delete non existent node
head.delete_node(15)
