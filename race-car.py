class Solution:
    def racecar(self, target: int) -> int:
        pos = deque()
        pos.append((0, 1, 0))
        visited = set()

        while pos:
            s, v, move = pos.popleft()
            visited.add((s, v))
            if s == target:
                return move

            fwdS = s + v
            fwdV = 2 * v
            if fwdS >= 0:
                if (fwdS, fwdV) not in visited:
                    visited.add((fwdS, fwdV))
                    pos.append((fwdS, fwdV, move + 1))

            backS = s
            backV = None
            if v < 0:
                backV = 1
            else:
                backV = -1

            if backS >= 0:
                if (backS, backV) not in visited:
                    visited.add((backS, backV))
                    pos.append((backS, backV, move + 1))
            
        return -1