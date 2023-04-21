import numpy as np 
inp = int(input())
ans = []
for _ in range(inp):
    ro1 = list(map(int, input().split()))
    ro2 = list(map(int, input().split()))
    arr = np.array([ro1, ro2])
    res = "NO"
    for i in range(4):
        if (arr[0][0] < arr[0][1]) and (arr[0][0] < arr[1][0]) and (arr[1][0] < arr[1][1]) and (arr[0][1] < arr[1][1]):
            res = "YES"
            break
        else:
            arr = np.rot90(arr, k=1)
    
    ans.append(res) 

for j in ans:
    print(j)



