class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingDependency = defaultdict(list)
        depCount = defaultdict(int)
        n = len(recipes)

        for i in range(n):
            ing = ingredients[i]
            for j in range(len(ing)):
                ingDependency[ing[j]].append(recipes[i])

            depCount[recipes[i]] += (len(ing))
        
        queue = deque()
        for i in supplies:
            queue.append(i)
        ans = []
        while queue:
            cur_sup = queue.popleft()
            childs = ingDependency[cur_sup]
            
            for i in range(len(childs)):
                child = childs[i]
                depCount[child] -= 1
                
                if depCount[child] == 0:
                    ans.append(child)
                    queue.append(child)
            
        return ans