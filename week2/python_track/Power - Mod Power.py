# Enter your code here. Read input from STDIN. Print output to STDOUT
base = int(input())
exponent = int(input())
mod = int(input())

power = base ** exponent
reminder = power % mod
print(power)
print(reminder)
