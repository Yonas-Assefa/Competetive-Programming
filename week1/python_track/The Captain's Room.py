# Enter your code here. Read input from STDIN. Print output to STDOUT
groupSize = int(input())
roomList = input()
roomNo = roomList.split(" ")


#logic
roomCount = {}
for i in roomNo:
    roomCount[i] = roomCount.get(i, 0) + 1
for i in roomCount:
    if roomCount[i] == 1:
        print(i)
        break
