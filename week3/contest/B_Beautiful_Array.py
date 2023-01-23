length = int(input())
array = list(map(int, input().split(" ")))

left = 0
right = 0
set1 = set()
set2 = set()
set3 = set()

while right < length:

    if array[right] == 0:
        set3.add(array[right])
        right += 1
        left = right
    elif array[right] < 0:
        temp = right
        while array[right] < 0:
            right += 1
        for i in range(temp, temp + 1):
            set2.add(array[i])
        
