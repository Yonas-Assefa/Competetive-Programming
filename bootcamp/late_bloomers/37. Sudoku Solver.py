class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    tempRow = i // 3
                    tempCol = j // 3
                    box[(tempRow, tempCol)].add(board[i][j])
        # print(cols, rows, box)
        def isValid(row, col, num, board):
            if (num in cols[col]) or (num in rows[row] )or (num in box[(row // 3, col // 3)]):
                return False
            return True

        def sudokuPlacement(row, col, n, board):
            if row == n:
                return True
            if col == n:
                return sudokuPlacement(row + 1, 0, n, board)
            if board[row][col] != ".":
                    return sudokuPlacement(row, col + 1, n, board)
            # print(row, col)
            for num in range(1, 10):
                if isValid(row, col, str(num), board):
                    cols[col].add(str(num))
                    rows[row].add(str(num))
                    box[(row // 3, col // 3)].add(str(num))
                    board[row][col] = str(num)
                    if sudokuPlacement(row, col + 1, n, board):
                        return True

                    #backtrack by undoing our current update
                    cols[col].discard(str(num))
                    rows[row].discard(str(num))
                    box[(row // 3, col // 3)].discard(str(num))
                    board[row][col] = "."
            return False

        n = len(board)
        sudokuPlacement(0, 0, n, board)



