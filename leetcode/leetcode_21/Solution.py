class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1) # dummy node
    current = dummy      # pointer to build the merged list

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next # move the pointer forward

    # Append the remaining elements of list1 or list2
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list = mergeTwoLists(list1, list2)
node = list
while node:
    print(node.val, " ")
    node = node.next
