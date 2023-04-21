ing = int(input())
ing_list = list(map(int,  input().split()))

pre_sum = [ing_list[0]]
post_sum = [ing_list[-1]]
for i in range(1,ing):
    pre_sum.append(pre_sum[-1] + ing_list[i])

for j in range(ing - 2, -1, -1):
    post_sum.append(post_sum[-1] + ing_list[j])
post_sum.reverse()
# print(post_sum, pre_sum)

ed = 0
alpho = 0
top = 0
botm = ing - 1
while top < botm:
    if pre_sum[top] < post_sum[botm]:
        top += 1
        ed += 1
    elif pre_sum[top] > post_sum[botm]:
        botm -= 1
        alpho += 1
    else:
        alpho += 1
        ed += 1
        top += 1
        botm -= 1

if top == botm:
    if pre_sum[top] <= post_sum[botm]:
        ed += 1
    else:
        alpho += 1

print(ed, alpho)





    