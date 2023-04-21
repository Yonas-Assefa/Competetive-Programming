ans = []
test = int(input())
for _ in range(test):
    stud = int(input())
    weight = list(map(int,input().split()))
    
    if stud < 18:
        if stud <= 12:
            ans.append(sum(weight))
        else:
            ans.append(sum(weight[12:stud]))
    else:
        
        def buss():
            left = left + 12
            minBus = min(buss(),buss())