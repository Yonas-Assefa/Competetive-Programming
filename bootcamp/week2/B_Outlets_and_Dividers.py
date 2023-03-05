ans = []
test = int(input())
for _ in range(test):
    stud, divd = list(map(int,input().split()))
    if divd:
        dividers = list(map(int,input().split()))
        dividers.sort()
        revDevid = dividers[::-1]
        
        if stud <= 2:
            ans.append(0)
        elif sum(revDevid) < stud:
            ans.append(-1)
        else:
            dev = revDevid[0]
            for i in range(1,divd):
                if dev >= stud:
                    ans.append(i)
                    break
                else:
                    dev += revDevid[i]
    else:
        if stud <= 2:
            ans.append(0)
        else:
            ans.append(-1)

       
for a in ans:
    print(a)
        