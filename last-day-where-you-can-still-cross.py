class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        left = 0
        right = len(cells)
        
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # print(land_matrix)

        def bfs(curDay):
            land_matrix = [[0] * col for i in range(row)]
            for i in range(curDay):
                x = cells[i][0] - 1
                y = cells[i][1] - 1
                # print(x, y)

                land_matrix[x][y] = 1
            
            land_queue = deque()
            for i in range(col):
                if land_matrix[0][i] == 0:
                    land_queue.append((0, i))
            # print((land_queue))
            while land_queue:
                cur = land_queue.popleft()
                rw = cur[0]
                cl = cur[1]
                if rw == (row - 1):
                    return True

                for i in range(4):
                    newRow = rw + directions[i][0]
                    newCol = cl + directions[i][1]
                    if self.isValid(row, col, newRow, newCol):
                        # print("here", newRow, newCol)
                        if land_matrix[newRow][newCol] == 0:
                            land_matrix[newRow][newCol] = 1
                            land_queue.append((newRow, newCol))
            return False

        lastDay = 0
        while left < right:
            mid = left + ((right - left) // 2)
            # print(mid)
            resp = bfs(mid)
            # print(resp)
            if resp:
                lastDay = mid
                left = mid + 1
            else:
                right = mid
        
        return lastDay






    
    def isValid(self, row, col, curRow, curCol):
        if curRow < row and curRow >= 0 and curCol < col and curCol >= 0:
            return True
        return False