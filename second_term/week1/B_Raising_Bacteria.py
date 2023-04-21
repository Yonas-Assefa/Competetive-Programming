n  = int(input())
# if (bac & (bac - 1) == 0):
#     print(1)
# else:
#     print(2)

bac = 0
temp = 0
while 2 ** temp <= n:

    while 2 ** temp <= n:
        temp += 1
    
    temp -= 1
    n -= (2 ** temp)
    temp = 0
    bac += 1
print(bac)