# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odd = ListNode(None)
        even = ListNode(None)
        oddHead = odd
        evenHead = even

        while head and head.next:
            odd.next = head
            odd = odd.next

            even.next = head.next
            even = even.next

            head = head.next.next

        if head:
            odd.next = head
            odd = odd.next

        even.next = None
        odd.next = evenHead.next
        
        return oddHead.next

