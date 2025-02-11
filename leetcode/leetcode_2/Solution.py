class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def addTwoNumbers(l1: ListNode, l2:ListNode) -> ListNode:
        dummy = ListNode() # Dummy node to simplify list creation
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10 # carry for the next digit
            current.next = ListNode(total % 10) # create a new node with the unit place digit
            current = current.next

            # Move the next node
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next # return the actual head    

