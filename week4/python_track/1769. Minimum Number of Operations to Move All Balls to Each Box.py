class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        boxes_lst=[int(i) for i in boxes]
        box_len = len(boxes_lst)
      
        for i in range(box_len):
            oprn_num = 0

            for j in range(box_len):
                if (j != i) and (boxes_lst[j] == 1):
                    sets = j - i
                    if sets < 0:
                        sets *= -1
                    oprn_num += sets
            ans.append(oprn_num)
        return ans

