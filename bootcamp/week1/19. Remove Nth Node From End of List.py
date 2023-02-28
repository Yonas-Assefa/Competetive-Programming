# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        countT = 1
        cur = head
        while cur and cur.next:
            countT += 1
            cur = cur.next
        
        n = (countT - n) + 1

        if n == 1:
            return head.next
    
        count = 1
        cur = head
        temp = None
    
        while count < n:
            temp = cur
            cur = cur.next
            count += 1
        
        temp.next = cur.next
        return head

        



        
        


