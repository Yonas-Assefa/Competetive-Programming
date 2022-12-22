class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_dict = {}
        for i in s:
            counter_dict[i] = counter_dict.get(i, 0) + 1
        for i in t:
            if i in counter_dict.keys():
                counter_dict[i] -= 1
                if counter_dict[i] == 0:
                    del counter_dict[i]
            else:
                return i