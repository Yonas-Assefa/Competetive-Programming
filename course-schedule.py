class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
        # Count incoming edges for each node
            incoming[course] += 1

        # Enqueue all nodes with no incoming edges
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
            # Current node is removed, so neighbor
            # has one less incoming edge.
                incoming[neighbor] -= 1
                # If neighbor has no remaining incoming
                # edges, it can now be processed.
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        # Why?
        if len(order) != numCourses:
            return False
        return True



        # mapping = { C:[] for C in range(numCourses)}
        # for course, pre in prerequisites:
        #     mapping[course].append(pre)
        # visited = set()
        # def dfs(course):
        #     if course in visited:
        #         return False
        #     if mapping[course] == []:
        #         return True
        #     visited.add(course)
        #     for pre in mapping[course]:
        #         if not dfs(pre): 
        #             return False

        #     visited.remove(course)
        #     mapping[course] = []
        #     return True

        # for course in range(numCourses):
        #     if not dfs(course): 
        #         return False

        # return True