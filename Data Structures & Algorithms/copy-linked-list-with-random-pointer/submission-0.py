"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup=dict()
        curr=head
        while curr:
            lookup[curr]=Node(curr.val)
            curr=curr.next
        # now create a dummy 
        dummy=trav=Node(0)
        while head:
            
            # now check if random also exist or not
            if head.random in lookup:
                lookup[head].random=lookup[head.random]
            trav.next=lookup[head]
            trav=trav.next
            head=head.next

        return dummy.next
        