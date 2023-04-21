ans = []
test = int(input())

for _ in range(test):
    wt, et, ef = list(map(int,input().split()))

    if et >= wt:
        ans.append(wt * 4)
    else:
        minT = float("inf")

        def minTime(elvFlr, redFlr,minT):
            if redFlr > elvFlr:
                return minT
            
            redWalk = elvFlr - redFlr
            time = (redWalk * wt) + ((elvFlr - redWalk) * et) + ((4 - redWalk) * et)
            minT = min(minT, time)
            # print(minT, elvFlr,redFlr)
            return minTime(elvFlr, redFlr + 1,minT)

        val = minTime(ef, 0,minT)
        # print(val)
        ans.append(val)
for a in ans:
    print(a)
