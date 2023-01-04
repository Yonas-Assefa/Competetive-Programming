no_test = int(input())
ans = []

def numberReplacment(length, numbers, letters):
    num_letter_match = {}

    for i in range(length):
        num = numbers[i]
        ltr = letters[i]

        if num in num_letter_match:
            if num_letter_match[num] != ltr:
                return "NO" 
        else:
            num_letter_match[num] = ltr

    return "YES"

for i in range(no_test):
    length = int(input())
    numbers = list(map(int,input().split(" ")))
    letters = input()
    result = numberReplacment(length, numbers, letters)
    ans.append(result)

for i in ans:
    print(i)