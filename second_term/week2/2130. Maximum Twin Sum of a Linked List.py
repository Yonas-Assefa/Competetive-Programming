# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # lst = []
        # while head:
        #     lst.append(head.val)
        #     head = head.next
        # result = [sum(i) for i in zip(lst, lst[::-1])]
        # return max(result)   
        prev = None
        cur = head
        count = 0
        while cur:
            temp = cur.next
            node = ListNode(cur.val)
            node.next = prev
            prev = node
            cur = temp
            count += 1  

        top = head
        botm = prev
        maxSum = -float("inf")
       
        for i in range(count // 2):
            maxSum = max(maxSum, top.val + botm.val)
            top = top.next
            botm = botm.next
        return maxSum
       
