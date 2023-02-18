import itertools
half = int(input())
arr = list(map(int, input().split()))
lst_sum = sum(arr) / 2
flag = False

all_permutations = list(itertools.permutations(arr)) 
for comb in all_permutations:
    comb_list = list(comb)
    if sum(comb_list[:half]) != lst_sum:
        string = ""
        for j in comb:
            string += str(j) + " "
        print(string)
        flag = True
        break
if flag == False:
    print("-1")


    

