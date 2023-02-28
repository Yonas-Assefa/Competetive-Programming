class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right, maxFruit, fruitCount = 0, 0, 0, {}
        
        while right < len(fruits):
            fruitCount[fruits[right]] = fruitCount.get(fruits[right], 0) + 1
            while len(fruitCount) > 2:
                fruitCount[fruits[left]] -= 1
                if fruitCount[fruits[left]] == 0:
                    del fruitCount[fruits[left]]
                left += 1
            maxFruit = max(maxFruit, right - left + 1)
            right += 1
        return maxFruit
    

        