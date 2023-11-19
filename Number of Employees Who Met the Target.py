class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        n = len(hours)
        breakPoint = n
        for i in range(n):
            if hours[i] >= target:
                breakPoint = i
                break

        return (n - breakPoint)
