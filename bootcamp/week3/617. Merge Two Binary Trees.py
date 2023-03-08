# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = TreeNode()
        ansP = ans
        if not root1 and not root2:
            return 
        if root1 and root2:
            ans.val = root1.val + root2.val
            ans.left = self.mergeTrees(root1.left, root2.left)
            ans.right = self.mergeTrees(root1.right, root2.right)
        elif root1 and not root2:
            ans.val = root1.val
            ans.left = self.mergeTrees(root1.left, None)
            ans.right = self.mergeTrees(root1.right, None)

        elif root2 and not root1:
            ans.val = root2.val
            ans.left = self.mergeTrees(None, root2.left)
            ans.right = self.mergeTrees(None, root2.right)
        return ans


        
        