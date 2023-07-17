class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    # Check if the linked list is empty or contains only one node
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    # Move the slow pointer one step at a time and the fast pointer two steps at a time
    while slow != fast:
        # If the fast pointer reaches the end of the linked list, there is no cycle
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    # If the slow and fast pointers meet, there is a cycle in the linked list
    return True

# Create a linked list with a cycle
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1  # Create a cycle

has_cycle = hasCycle(head)
print(has_cycle) 

"""
Question12:

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""