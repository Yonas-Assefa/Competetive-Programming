ans = []
test = int(input())
for _ in range(test):
    stud, divd = list(map(int,input().split()))
    if divd:
        dividers = list(map(int,input().split()))
        dividers.sort()
        revDevid = dividers[::-1]
        
        # if stud <= 2:
        #     ans.append(0)
        # elif sum(revDevid) < stud:
        #     ans.append(-1)
        # else:
        dev = 2
        flag = False

        for i in range(divd):
            if dev >= stud:
                ans.append(i)
                flag = True
                break
            dev += (revDevid[i] - 1)

        if (not flag) and dev >= stud:
            ans.append(divd)
        elif dev < stud:
            ans.append(-1)
           
    else:
        if stud <= 2:
            ans.append(0)
        else:
            ans.append(-1)

       
for a in ans:
    print(a)
        