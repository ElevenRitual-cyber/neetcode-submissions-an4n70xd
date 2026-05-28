# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(temp):
            count=0
            while temp:
                temp=temp.next
                count+=1
            return count
        nth=helper(head)-n
        if nth==0:
            return head.next
        prev=None
        curr=head
        while curr and nth:
            prev=curr
            curr=curr.next
            nth-=1

        prev.next=curr.next
        return head

