no_test = int(input())
ans = []
 
for i in range(no_test):
    shirt_size = list(input().split(" "))
    size_order = {  "S" : 0,
                    "M" : 1,
                    "L" : 2
                }
    shirt_one = len(shirt_size[0])
    shirt_two = len(shirt_size[1])
 
    if shirt_size[0][shirt_one - 1] == shirt_size[1][shirt_two - 1]:
        if shirt_size[0][shirt_one - 1] == "S":
            if shirt_one > shirt_two:
                ans.append("<")
            elif shirt_one == shirt_two:
                ans.append("=")
            else:
                ans.append(">")
        
        else:
            if shirt_one > shirt_two:
                ans.append(">")
            elif shirt_one == shirt_two:
                ans.append("=")
            else:
                ans.append("<")

    elif size_order[shirt_size[0][shirt_one - 1]] > size_order[shirt_size[1][shirt_two - 1]]:
        ans.append(">")
        
    else:
        ans.append("<")
 
for i in ans:
    print(i)
