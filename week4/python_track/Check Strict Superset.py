# Enter your code here. Read input from STDIN. Print output to STDOUT
#input
set_A = set(map(int, input().split()))
num_sets = int(input())

#logic
ans = True
for i in range(num_sets):
    temp_set = set(map(int, input().split()))
    diff1 = set_A - temp_set
    diff2 =  temp_set - set_A
    if len(diff1) == 0 or len(diff2) > 0:
        ans = False
        break
print(ans)
        