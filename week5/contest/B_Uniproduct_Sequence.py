seq_leng = int(input())
seq = list(map(int, input().split()))

negCount = 0
zeroCount = 0
coin = 0
for i in seq:
    if i < 0:
        coin += ((-1 - i))
        negCount += 1
    elif i > 0:
        coin += (i - 1)
     
    else:
        coin += 1
        zeroCount += 1
 
if negCount % 2 != 0:
    if zeroCount > 0:
        coin += 0
    else:
        coin += 2

print(coin)
