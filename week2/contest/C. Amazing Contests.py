no_contest = int(input())
contests = input()
contest_list = list(map(int,contests.split(" ")))
amazing = 0
best = contest_list[0]
worst = contest_list[0]
for i in range(1, no_contest):
    if contest_list[i] < worst:
        amazing += 1
        worst = contest_list[i]
    elif contest_list[i] > best:
        amazing += 1
        best = contest_list[i]
print(amazing)