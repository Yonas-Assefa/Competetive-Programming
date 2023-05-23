class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        if grid[0][0] or grid[n - 1][m - 1] :
            return -1
        if n == m == 1:
            return 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
       
        path = deque()
        path.append((0, 0, 1))
        visited = set()
        while path:
            cur = path.popleft()
            visited.add((cur[0], cur[1]))
            for x in range(-1, 2):
                for y in range(-1, 2):

                    newRow = cur[0] + x
                    newCol = cur[1] + y

                    if newRow in range(n) and newCol in range(m):
                        if grid[newRow][newCol] == 0:
                            if (newRow, newCol) not in visited:
                                visited.add((newRow, newCol))
                                if (newRow, newCol) == (n - 1, m - 1):
                                    return (cur[2] + 1)
                                path.append((newRow, newCol, cur[2] + 1))
        
        return -1