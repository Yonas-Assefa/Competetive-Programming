class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(row, col, board):
            cols = set()
            for i in range(9):
                if board[i][col] != ".":
                    if board[i][col] in cols:
                        return False
                    cols.add(board[i][col])

            rows = set()
            for i in range(9):
                if board[row][i] != ".":
                    if board[row][i] in rows:
                        return False
                    rows.add(board[row][i])
            
            # newRow = (row // 3)  * 3
            # newCol = (col // 3)  * 3
            if row % 3 == 0 and col % 3 == 0:
                box = set()
                for i in range(row, row + 3):
                    for j in range(col , col + 3):
                        temp = board[i][j]
                        if temp != ".":
                            if temp in box:
                                print(row, col, "flase")
                                return False
                            box.add(temp)
            return True

        for i in range(9):
            for j in range(9):
                if not isValid(i, j, board):
                    return False
        
        return True



