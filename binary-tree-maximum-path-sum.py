# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.absmax = root.val

        def dfs(cur):
            if not cur:
                return 0
            left = max(0, dfs(cur.left))
            right = max(0, dfs(cur.right))

            self.absmax = max(self.absmax, left + right + cur.val)
            return cur.val + max(left, right)
            

        dfs(root)
        return self.absmax