class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        visited = set()
      
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0: 
                    q.append((i, j))
                    visited.add((i, j))
                else:
                    mat[i][j] = 0
                
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
                    visited.add((nr, nc)) 
        return mat