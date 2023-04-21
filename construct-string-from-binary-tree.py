class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""  # base case: empty tree
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if left == "" and right == "":
            return str(root.val)
        elif left == "":
            return str(root.val) + "()" + "(" + right + ")"
        elif right == "":
            return str(root.val) + "(" + left + ")"
        else:
            return str(root.val) + "(" + left + ")" + "(" + right + ")"