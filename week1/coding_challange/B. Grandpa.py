grandpa_collection = input().split(" ")
unique_stone = {}
for i in grandpa_collection:
    unique_stone[i] = unique_stone.get(i, 0) + 1
if len(unique_stone) >= 5:
    print("YES")
else:
    print("NO")
    