class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        lockList = deque()
        lockList.append(["0000", 0])
        visited = set()
        deadends = set(deadends)

        def children(curLock):
            moves = []
            for i in range(4):
                #roll to the front
                move = str((int(curLock[i]) + 1) % 10)
                nxtMove = curLock[:i] + move + curLock[i + 1 : ]
                moves.append(nxtMove)

                #roll backward
                move = str((int(curLock[i]) - 1 + 10) % 10)
                nxtMove = curLock[:i] + move + curLock[i + 1 : ]
                moves.append(nxtMove)
            
            return moves


        while lockList:
            curTurn, turns = lockList.popleft()
            if curTurn == target:
                return turns
            
            for child in children(curTurn):
                if child not in visited and child not in deadends:
                    visited.add(child)
                    lockList.append([child, turns + 1])
        
        return -1