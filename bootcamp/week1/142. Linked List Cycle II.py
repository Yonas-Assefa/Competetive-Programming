# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node = head
        # node_set = set()
        # while node:
        #     if node not in node_set:
        #         node_set.add(node)
        #         node = node.next
        #     else:
        #         return node
        # return None
        if not head:
            return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next               
                return slow
        return None










