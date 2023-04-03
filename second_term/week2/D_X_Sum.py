def addDiagonal(curRow, curCol, chess):
    row = len(chess)
    col = len(chess[0])

    topLeft = 0
    topRight = 0
    botmLeft = 0
    botmRight = 0
    top = curRow
    botm = curRow
    left, right = curCol, curCol
    while top >= 0 or botm < row:
        if left >= 0 and top >= 0:
            topLeft += chess[top][left]
        if right < col and top >= 0:
            topRight += chess[top][right]

        if left >= 0 and botm < row:
            botmLeft += chess[botm][left]

        if right < col and botm < row:
            botmRight += chess[botm][right]
        
        top -= 1
        botm += 1
        left -=  1
        right +=  1
    

    total = topLeft + topRight + botmLeft + botmRight - (3 * chess[curRow][curCol])
    return total

test = int(input())
ans = []

for _ in range(test):
    n, m = list(map(int, input().split()))
    chess = []
    for i in range(n):
        temp = list(map(int, input().split()))
        chess.append(temp)
    
    res = 0
    for i in range(n):
        for j in range(m):
            val = addDiagonal(i, j, chess)
            res = max(res, val)
    ans.append(res)

for i in ans:
    print(i)