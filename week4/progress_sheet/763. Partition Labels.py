class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        nums_index = {char : indx for indx, char in enumerate(s)}
        ans = []
        left = 0
        right = 0

        for indx, char in enumerate(s):
            right = max(right, nums_index[char])

            if indx == right:
                ans.append(indx - left + 1)
                left = right + 1
        
        return ans
            
