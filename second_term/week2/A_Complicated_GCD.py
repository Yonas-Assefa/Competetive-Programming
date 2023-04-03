def GDC(num1, num2):
    if num2 == 0:
        return num1
    return GDC(num2, num1 % num2)

a, b = list(map(int, input().split()))

if a == b:
    print(a)
else:
    divider = GDC(a, a + 1)
    ans = divider
    for i in (a + 2, b + 1):
        if i % divider != 0:
            ans = 1
            break
    print(divider)
    
