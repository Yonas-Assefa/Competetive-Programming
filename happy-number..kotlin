class Solution:
    def isHappy(self, n: int) -> bool:
        used = []

        while(n>0):
            tmp = 0
            while(n>0):
                i = n%10

                tmp += i*i
                n = n//10

            if(tmp in used):
                return False
            else:
                used.append(tmp)

            if(tmp==1):
                return True
            
            n = tmp

        return False