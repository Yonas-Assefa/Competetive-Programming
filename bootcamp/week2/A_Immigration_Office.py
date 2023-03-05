ans = []
n = int(input())
names = list(input().split())
test = int(input())
for _ in range(test):
    name = input()
    left = 0
    right = n - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if name == names[mid]:
            break
        elif name < names[mid]:
            right = mid 
        else:
            left = mid + 1
    if left == n - 1:
        if name <= names[left]:
            ans.append(left)
        else:
            ans.append(left + 1)
    else:
        ans.append(left)

for a in ans:
    print(a)
