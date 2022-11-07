class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k<chalk[0]:
            return 0
        rem= k % sum(chalk)
        i=0
        while rem>=0:
            rem-=chalk[i]
            i+=1
        return i-1
