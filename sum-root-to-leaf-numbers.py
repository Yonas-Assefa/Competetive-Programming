# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, "")
        return self.ans
    
    def dfs(self, curNode, curNum ):
        if not curNode:
            return
        if not curNode.left and not curNode.right:
            self.ans += int(curNum + str(curNode.val))

        self.dfs(curNode.left, curNum + str(curNode.val))
        self.dfs(curNode.right, curNum + str(curNode.val))