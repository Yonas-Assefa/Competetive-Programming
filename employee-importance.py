class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        D = {i.id : e for e, i in enumerate(employees)}
        def dfs(id):
            ans = employees[D[id]].importance
            for i in employees[D[id]].subordinates:
                ans += dfs(i)
            return ans
        return dfs(id)