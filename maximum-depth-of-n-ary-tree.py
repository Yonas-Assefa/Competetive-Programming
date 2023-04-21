# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # if not root:
        #     return 0
        # max_depth = 0
        # for child in root.children:
        #     max_depth = max(max_depth, self.maxDepth(child))
            
        # return max_depth + 1
        return self.dfs(root)

    def dfs(self, curNod):
        if not curNod:
            return 0
        maxDepth = 0
        for child in curNod.children:
            maxDepth  = max(maxDepth, self.maxDepth(child))
        return maxDepth + 1