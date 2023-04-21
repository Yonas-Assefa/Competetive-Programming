# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = ""
        num2 = ""
        
        #extract the Linked list value as a singele number digits
        while l1 or l2:

            if l1:
                num1 += str(l1.val)
                l1 = l1.next

            if l2:
                num2 += str(l2.val)
                l2 = l2.next

        #reverse digits of the number
        num1 = num1[::-1]
        num2 = num2[::-1]

        listSum = int(num1) + int(num2)
        sumStr = str(listSum)
        sumLen = len(sumStr)

        cur = ListNode(None)
        curPointer = cur

        #constracting linkedlist of digits the sum
        for i in range(sumLen - 1, -1, -1):

            val = int(sumStr[i])
            cur.next = ListNode(val)
            cur = cur.next

        return curPointer.next
        
            