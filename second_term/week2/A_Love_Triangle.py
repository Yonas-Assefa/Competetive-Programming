n = int(input())
love = list(map(int, input().split()))
ans = "NO"
for i in range(1, n + 1):
    first = i
    second = love[first - 1]
    third = love[second - 1]
    fourth = love[third - 1]
    if first == fourth and third != first and third != second:
        ans = "YES"
        break
print(ans)

    
