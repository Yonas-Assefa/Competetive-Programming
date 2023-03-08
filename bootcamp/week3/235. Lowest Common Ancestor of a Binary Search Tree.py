# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        minNode = min(p.val, q.val)
        maxNode = max(p.val, q.val)

        if root.val >= minNode and root.val <= maxNode:
            return root

        elif root.val < minNode:
            return self.lowestCommonAncestor(root.right, p, q)

        elif root.val > maxNode:
            return self.lowestCommonAncestor(root.left, p, q)
