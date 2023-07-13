# optimised code to merge two linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two lists
merged_list = mergeTwoLists(list1, list2)

# Print the merged list
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

"""
Question3: Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""