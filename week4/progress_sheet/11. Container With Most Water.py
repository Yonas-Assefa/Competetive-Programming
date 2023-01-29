class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftP = 0
        rightP = len(height) - 1
        max_water = 0

        while leftP < rightP:
            max_water = max(max_water, min(height[leftP], height[rightP]) * (rightP - leftP))
            print(max_water)
            if height[leftP] > height[rightP]:
                rightP -= 1
            else:
                leftP += 1
        return max_water