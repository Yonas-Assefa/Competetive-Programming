# Enter your code here. Read input from STDIN. Print output to STDOUT
def piling(lst):
    left = 0
    right = n - 1
    if lst[right] > lst[left]:
        current = lst[right]
        right -= 1
    else:
        current = lst[left]
        left += 1
    while left < right:
        
        if (current < lst[left]) or (current < lst[right]):
            return "No"
        else:
            if lst[right] > lst[left]:
                current = lst[right]
                right -= 1
            else:
                current = lst[left]
                left += 1
    return "Yes"
          
T = int(input())
for i in range(T):
    n = int(input())
    listInput = input()
    lst = list(map(int,listInput.split(" ")))
    print(piling(lst))
    
    
