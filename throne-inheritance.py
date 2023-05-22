class ThroneInheritance:

    def __init__(self, kingName: str):

        self.parentList = defaultdict(list)
        self.king = kingName
        self.parentList[self.king] = []
        self.deadList = set()
               
    def birth(self, parentName: str, childName: str) -> None:
        self.parentList[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deadList.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        order = []
        self.dfs(self.king, order, set())
        return order
    
    def dfs(self, cur, order, visited):
        if cur not in self.deadList:
            order.append(cur)
            visited.add(cur)

        for child in self.parentList[cur]:
            if child not in visited:
                self.dfs(child, order, visited)
        
        
    
    
    

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()