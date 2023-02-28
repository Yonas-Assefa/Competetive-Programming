# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        temp = head
        cnt = 1
        while temp.next:
            temp = temp.next
            cnt += 1
        temp.next = head
        k = cnt - (k % cnt)
        while k > 0:
            temp = temp.next
            k -= 1
        newHead = temp.next
        temp.next = None
        return newHead
                    