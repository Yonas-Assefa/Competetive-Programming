# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
integer_list = map(int, input().split())
tup = ()
for x in integer_list:
    tup+=(x,)

print(hash(tup))

