no_of_input = int(input())
for i in range(no_of_input):
    width = int(input())
    height = int(input())
    friend_no = int(input())

    no_sheets = 1
    while width % 2 == 0:
        no_sheets *= 2
        width /= 2
    
    while height % 2 == 0:
        no_sheets *= 2
        height /= 2
    
    if no_sheets >= friend_no:
        print("YES")
    else:
        print("NO")
    