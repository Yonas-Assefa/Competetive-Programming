lines = int(input())
stack = []
add = 0
x = 0
overflow = False

for line in range(lines):
    para = input()
    if "add" in para:
        if not stack:
            x += 1
        else:
            add += 1
    
    elif "for" in para:
        if not stack:
            stack.append(para[4:])
        else:
            temp =str(int(stack[-1]) * int(para[4:]))     
            stack.append(temp)
    elif "end" in para:
        if x > (2** 32 - 1):
            overflow = True
            break
        val = add
        add = 0
        multi = int(stack.pop())
        x += (val * multi)

        

if not overflow:
    print(x)
else:
    print("OVERFLOW!!!")



    