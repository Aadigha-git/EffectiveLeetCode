class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle_node = findMiddleNode(head)
print(middle_node.val)
