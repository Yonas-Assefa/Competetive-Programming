# Enter your code here. Read input from STDIN. Print output to STDOUT

#input
no_english = int(input())
english_subscription = set(map(int, input().split(" ")))

french_no = int(input())
french_subscription = set(map(int, input().split()))

#logic
english_only = english_subscription - french_subscription

print(len(english_only))
