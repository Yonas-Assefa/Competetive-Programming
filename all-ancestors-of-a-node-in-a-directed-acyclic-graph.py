class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        #BFS
        
        adjList = defaultdict(list)
        incomings = defaultdict(int)
        ans = [set() for i in range(n)]

        for parent, child in edges:
            adjList[parent].append(child)
            incomings[child] += 1
        
        queue = deque()
        for i in range(n):
            if not incomings[i]:
                queue.append(i)
        
        while queue:
            curNode = queue.popleft()
            for child in adjList[curNode]:
                ans[child].add(curNode)
                ans[child].update(ans[curNode])
                incomings[child] -= 1

                if not incomings[child]:
                    queue.append(child)

        ans = [sorted(i) for i in ans]
        return ans