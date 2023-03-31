test = int(input())
ans = []
for _ in range(test):
    x = int(input())
    count = 0
    copy = x
    flip  = 0
    firstOne = 0
    while copy > 0:
        if copy % 2 != 0:
            count += 1
        if count == 1:
            firstOne = flip
        copy = copy >> 1
        flip += 1
    
    
    res = 0
    if count > 1:
        fst1 = 0
        while x % 2 == 0:
            fst1 += 1
            x = x >> 1
        res = 2 ** fst1
    else:
        if firstOne:
            res = 2 ** firstOne + 1
        else:
            res = 3
    ans.append(res)
for i in ans:
    print(i)
# x = 4
# x = x >> 1
# print(x)
# print(4 >> 1)