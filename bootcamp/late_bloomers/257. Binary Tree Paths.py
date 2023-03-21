# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        res = ""

        def binaryPath(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res += (str(root.val))
                ans.append(res)
                res = res[: -1]
                return
            res += (str(root.val) + "->")
            binaryPath(root.left, res)
            binaryPath(root.right, res)
        
        binaryPath(root, res)
        return ans


