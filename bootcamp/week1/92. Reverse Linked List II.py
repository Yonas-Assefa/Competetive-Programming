# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
            
        part = ListNode(None)
        partHead = part
        prev = ListNode(None)
        prevHead = prev

        count = 1
        cur = head
        while count <= right:
            if count < left:
                prev.next = cur
                prev = prev.next
            else:
                part.next = cur 
                part = part.next
            count += 1
            cur = cur.next
        prev.next = part.next
        part.next = None
   

        partHead = partHead.next
        rev = None
        cur = partHead
        while cur:
            temp = cur.next
            cur.next = rev
            rev = cur
            cur = temp

        nxt = prev.next
        prev.next = rev

        partHead.next = nxt
        return prevHead.next
        




        
