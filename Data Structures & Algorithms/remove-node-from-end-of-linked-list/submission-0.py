# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        start = head

        while start:
            length+=1
            start = start.next

        if n>length:
            return None
        
        node = length-n

        if node == 0:
            return head.next

        curr = head
        prev = None

        for i in range(0,node):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return head