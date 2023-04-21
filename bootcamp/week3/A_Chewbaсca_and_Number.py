num = int(input())
val = ""

while num > 10:
    temp = num % 10
    if 9 - temp < temp:
        val = str(9 - temp) + val
    else:
        val = str(temp) + val
    
    num = num // 10

if num == 9 or (9 - num > num):
    val = str(num) + val
else:
    val = str(9 - num) + val
print(int(val))













# val = ""
# # print(val, num_arr)
# for i in range(len(num_arr) - 1, 0,-1):
#     # print(num_arr[i],i)
#     if int(num_arr[i]) >= 5:
#         temp = 9 - int(num_arr[i])
#         val = val + str(temp)
#         # print(val, int(num_arr[i]),temp)
#     else:
        
#         val = val + num_arr[i]
#         # print(val)

# if int(num_arr[0]) >= 5 and int(num_arr[0]) != 9:
#     # print(val, int(num_arr[i]))
#     temp = 9 - int(num_arr[0])
#     val = str(temp) + val
# else:
    
#     val = num_arr[0] + val
# # print(val)
# print(int(val))
# l = 0
# r = 0
# while r < len(val) and val[r] == "0":
#     r += 1
# if r == len(val):
#     print(0)
# else:
#     val = val[r:]
#     print(int(val))
