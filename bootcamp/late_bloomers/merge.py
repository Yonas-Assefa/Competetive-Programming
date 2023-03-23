def merge(list1, list2):
    top = 0
    botm = 0
    res = []

    while top < len(list1) and botm < len(list2):
        if list1[top] < list2[botm]:
            res.append(list1[top])
            top += 1
        else:
            res.append(list1[botm])
            botm += 1
    
    res += list1[top: ]
    res += list2[botm: ]
    
    return res

def mergeSort(left, right, arr):
    # if left == right:
    #     return [arr[left]]
    if len(arr) == 1:
        return arr
    
    mid =  (right + left) // 2
    left_half = mergeSort(left, mid, arr[left : mid])
    right_half = mergeSort(mid + 1, right, arr[mid: right])

    return merge(left_half, right_half)

# def test():
#     assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
#     assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
#     assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
#     print("Great Job !!!")
# test()
res = [7,2,3,1,4]
print(mergeSort(0, 5, res))
