# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = list1, list2
        head,tail = None, None

        while left != None and right != None:
            if left.val<right.val:
                temp = ListNode(left.val)
                left = left.next
            else:
                temp = ListNode(right.val)
                right = right.next
            if head == None and tail == None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp

        while left != None:
            temp = ListNode(left.val)
            if head == None and tail == None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
            left = left.next

        while right != None:
            temp = ListNode(right.val)
            if head == None and tail == None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
            right = right.next

        return head

        