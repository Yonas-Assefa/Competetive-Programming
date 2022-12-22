# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input()
n,m = size.split(" ")
listItems = input()
lstItem = listItems.split(" ")
set1Input = input()
set1 = set(set1Input.split(" "))
set2Input = input()
set2 = set(set2Input.split(" "))

#logic
happines = 0
for i in lstItem:
    if i in set1:
        happines += 1
    elif i in set2:
        happines -= 1
print(happines)
