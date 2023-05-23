class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i,j,mark):
            nonlocal board
            if( (i < 0) or (j < 0 ) or (i >= m) or (j >= n) ):
                print(f'returned on {i,j}')
                return False;
            elif(board[i][j] == 'X' or board[i][j] == mark):
                return True
            else:
                res = True
                board[i][j] = mark
                for d in direc:
                    x = i+d[0]
                    y = j+d[1]
                    # if i put res before the function call 
                    # then once res has been set to false the 
                    # function call will never happen
                    res = dfs(x,y,mark) and res; 
                return res
        
        direc = [[-1,0],[0,-1],[1,0],[0,1]]
        m , n = len(board), len(board[0]);
        
        for i in range(0,m):
            for j in range(0,n):
                if( board[i][j] == "O" ):
                    print(f'checkng on i:{i} j:{j}')
                    if( dfs(i , j,'1') ): #check if not touching the boundry
                        dfs(i,j,"X") # if not then mark x 
        
        #Unmarks 1's to O's if the area touched the boundry
        for i in range(0,m):
            for j in range(0,n):
                if(board[i][j] == '1'): board[i][j] = "O"