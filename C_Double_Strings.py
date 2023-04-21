test = int(input())
ans = []
for _ in range(test):

    str_no =  int(input())
    lst_arr = []
    for i in range(str_no):
        word = input()
        lst_arr.append(word)
    
    res = ""
    for i in range(str_no):
        string = lst_arr[i]
        out = "0"
        for j in range(str_no):
            for k in range(str_no):
                if j != i and k != i:
                    if string == lst_arr[j]  + lst_arr[k]:
                        out = "1"
                        break
            if out == "1":
                break
        res += out
    
    ans.append(res)

for r in ans:
    print(r)