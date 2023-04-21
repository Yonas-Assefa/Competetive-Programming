test = int(input())
ans = []
for _ in range(test):
    n, m = list(map(int, input().split()))
    sold = input()
    soldList = list(sold)
    res = ""
    if n == 2:
        if "1" in sold:
            res = "11"
            ans.append(res)
        else:
            res = "00"
            ans.append(res)
        
    else:
        for i in range(min(n, m)):
            if soldList[0] == "0" and soldList[1] == "1":
                soldList[0] = "1"
            # print(n,m)
            left = 0
            right = 2
            dic = {}
            while right < n:
                if soldList[left + 1] == "0":
                   if (soldList[left] == "1" and soldList[right] == "0") or (soldList[left] == "0" and soldList[right] == "1" ):
                       dic[left + 1] = "1"
                left += 1
                right += 1

            if dic:
                # print(dic)
                for ind in dic:
                    soldList[ind] = dic[ind]

            
                    
                 
                
                    
            # print(soldList)
        ans.append("".join(soldList))        


for a in ans:
    print(a)