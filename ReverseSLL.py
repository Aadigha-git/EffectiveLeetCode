class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    previous = None
    current = head

    while current:
        # Store the next node
        next_node = current.next

        # Reverse the pointer
        current.next = previous

        # Move the pointers one step forward
        previous = current
        current = next_node

    # Return the new head (which is the last node of the original list)
    return previous

# linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reversed_head = reverseList(head)

current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next

"""
Questio18:

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""