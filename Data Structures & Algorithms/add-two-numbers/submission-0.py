# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        num1 = 0
        place = 1

        while curr:
            num1 +=  curr.val*place
            place = place*10
            curr = curr.next

        curr = l2
        num2 = 0
        place = 1
        while curr:
            num2 +=  curr.val*place
            place = place*10
            curr = curr.next
        total = num1 + num2
        if total == 0:
            return ListNode(0)

        head = None
        tail = None

        while total > 0:
            digit = total % 10
            node = ListNode(digit)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

            total //= 10

        return head
          