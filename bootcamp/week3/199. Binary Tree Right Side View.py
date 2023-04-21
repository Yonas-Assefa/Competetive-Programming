# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        levelNodes = collections.deque()
        levelNodes.append(root)

        while levelNodes:
            levelNum = len(levelNodes)
            level = []
            for i in range(levelNum):
                node = levelNodes.popleft()
                
                if node:
                    level.append(node.val)
                    levelNodes.append(node.left)
                    levelNodes.append(node.right)

            if level:
                ans.append(level.pop())
        
        return ans

            


