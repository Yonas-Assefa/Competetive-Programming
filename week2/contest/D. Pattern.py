num_patter = int(input())
patter_list = []
for i in range(num_patter):
    pattern = input()
    patter_list.append(pattern)
length = len(patter_list[0])
ans = ""
for i in range(length):
    word = set()
    for j in range(num_patter):
        word.add(patter_list[j][i])


    if len(word) == 1:
        for char in word:
            if char == "?":
                ans += "x"
            else:
                ans += char
    elif len(word) == 2 and "?" in word:
        for char in word:
            if char == "?":
                continue
            else:
                ans += char
    else:
        ans += "?"

print(ans)

