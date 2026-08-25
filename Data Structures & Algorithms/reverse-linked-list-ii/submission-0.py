# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or right==left:
            return head
        
        dummy=ListNode(0,head)
        left_prev=dummy
        for _ in range(left-1):
            left_prev=left_prev.next

        curr=left_prev.next
        prev=None

        while left<=right:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            left+=1

        left_prev.next.next=curr
        left_prev.next=prev

        return dummy.next        







        