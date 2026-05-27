# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(trav,prev):
            if trav is None:
                return prev
            t=trav.next
            trav.next=prev
            return reverse(t,trav)
        return reverse(head,None)
        