test = int(input())
ans = []

for _ in range(test):

    p, m = list(map(int, input().split()))
    count = min(min(p,m),( p + m) // 4)
    ans.append(count)
    
    # while (p) and (m) and (p + m >= 4):
    #     if p >= m :
    #         p = p - 3
    #         m = m - 1
    #     else:
    #         p = p - 1
    #         m = m - 3
    #     count += 1
    # print(count)


    # def teams(p,m,count):
    #     if (not p) or (not m) or (p + m < 4):
    #         return count
        
    #     if p >= m :
    #         p = p - 3
    #         m = m - 1
    #     else:
    #         p = p - 1
    #         m = m - 3
    #     count += 1
    #     # print(p,m,count)
    #     return teams(p,m,count)

    # val = teams(p,m,count)

    # ans.append(val)

for i in ans:
    print(i)



