def xor(temp, cur):
    xorVal = 0
    leng = len(temp)
    for i in range(leng):
        if i == cur:
            continue
        xorVal = xorVal ^ temp[i]
        # print(temp, xorVal)
    
    if temp[cur] == xorVal:
        return True
    return False

test  = int(input())
ans = []
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0

    for i in range(n):
        if xor(nums, i):
            ans.append(nums[i])
            break
for i in ans:
    print(i)