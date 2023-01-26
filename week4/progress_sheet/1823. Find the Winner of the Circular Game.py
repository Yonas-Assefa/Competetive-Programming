class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def get_index(cur_index, steps, cur_length):
            new_index = cur_index + steps - 1

            if new_index >= cur_length:
                new_index %= cur_length
            
            return new_index
        
        def get_ans(arr, index):
            length = len(arr)

            if length == 1:
                return arr[0]
            else:
                arr.pop(index)
                return get_ans(arr, get_index(index, k, length - 1))
        
        return get_ans([i for i in range(1, n + 1)], get_index(0, k, n))

