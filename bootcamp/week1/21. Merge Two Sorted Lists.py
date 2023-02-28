# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # top = list1
        # botm = list2
        # ans = ListNode(None)
        # ansHead = ans

        # while top and botm:
        #     if top.val < botm.val:
        #         ans.next = top
        #         ans = ans.next
        #         top = top.next

        #     else:
        #         ans.next = botm
        #         ans = ans.next
        #         botm = botm.next
        # print(ansHead.next)
        # if top:
        #     ans.next = top
        # else:
        #     ans.next = botm
        # return ansHead.next
        
        top = list1
        topHead = top
        botm = list2
        botmHead = botm

        while top and botm:
            if top.val < botm.val:
                temp = top.next
                top.next = botm
                top = temp
            else:
                temp = botm.next
                botm.next = top
                botm = temp
            print(top,"bo", botm)
        print(list2)
        
