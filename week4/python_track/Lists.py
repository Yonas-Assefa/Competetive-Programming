if __name__ == '__main__':
    N = int(input())
    list1 = []
    command_list = []
    for i in range(N):
        list2 = input().split()
        command_list.append(list2)
    for cmd in command_list:
        if cmd[0] == "insert":
            list1.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(list1)
        elif cmd[0] == "remove":
            list1.remove(int(cmd[1]))
        elif cmd[0] == "append":
            list1.append(int(cmd[1]))
        elif cmd[0] == "sort":
            list1.sort()
        elif cmd[0] == "pop":
            list1.pop()
        else:
            list1.reverse()
