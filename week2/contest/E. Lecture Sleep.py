input_list = list(map(int, input().split(" ")))
theorems_list = list(map(int, input().split(" ")))
awake = input()
awake_list = list(map(int, awake.split(" ")))

maxSum = 0
left = 0
right = input_list[1]
magic = 0

while right < input_list[0]:
    if awake_list[right] == 0:
        magic += 1
    
    tempSum = sum(theorems_list[left : right + 1])
    maxSum = max(maxSum, tempSum)
    left += 1
    right += 1
print(maxSum)

print(theorems_list)