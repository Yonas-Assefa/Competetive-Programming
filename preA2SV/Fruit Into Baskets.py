class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_dict={}
        left=0
        for right,fruit in enumerate(fruits):
            fruit_dict[fruit]=fruit_dict.get(fruit,0)+1
            
            if len(fruit_dict)>2:
                fruit_dict[fruits[left]]-=1
                if fruit_dict[fruits[left]]==0:
                    del fruit_dict[fruits[left]]
                left+=1
        return right-left+1
        
