# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy

        carry=0

        while l1 or l2 or carry:
            v1=v1.val if l1 else 0
            v2=v2.val if l2 else 0

            val=v2+v1+carry
            carry=val//10
            val=val%10

            curr.next=ListNode(val)

        return dummy.next
            