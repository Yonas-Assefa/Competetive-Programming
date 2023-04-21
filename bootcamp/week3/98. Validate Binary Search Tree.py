# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smaller(self, node, key):
        if not node:
            return True
        if node.val < key:
            return (self.smaller(node.left,key) and self.smaller(node.right, key) )
        else:
            return False

    def greater(self, node,key):
        if not node:
            return True
        if node.val > key:
            return( self.greater(node.left,key) and self.greater(node.right, key) )
        else:
            return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (self.smaller(root.left,root.val) and self.greater(root.right,root.val)):
            return (self.isValidBST(root.left) and self.isValidBST(root.right))
        else:
            return False
 