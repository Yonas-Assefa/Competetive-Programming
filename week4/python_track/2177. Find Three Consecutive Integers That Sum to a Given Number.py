class Solution:
    import math
    def sumOfThree(self, num: int) -> List[int]:
        start = (num - 3) / 3

        if ceil(start) == floor(start):

            start = int(start)
            return [start, start + 1, start + 2]
            
        else:
            return []