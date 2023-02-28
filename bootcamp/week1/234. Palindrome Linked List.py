# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        start = head
        end = prev
        while end:
            if end.val != start.val:
                return False
            start = start.next
            end = end.next
        
        return True
        
