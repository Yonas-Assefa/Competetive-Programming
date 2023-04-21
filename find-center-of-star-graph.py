# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         first = edges[0][0]
#         second = edges[0][1]
#         ans1 = True
#         ans2 = True
#         for edge in range(1, len(edges)):
#             if first not in edges[edge]:
#                 ans1 = False
#                 break
       
#         for edge in range(1, len(edges)):
#             if second not in edges[edge]:
#                 ans2 = False
#                 break
#         if ans1:
#             return first
#         else:
#             return second

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first=edges[0][0]
        second=edges[0][1]
        if edges[1][0]==first or edges[1][1]==first:
            return first
        return second
    #please upvote me it would encourage me alot