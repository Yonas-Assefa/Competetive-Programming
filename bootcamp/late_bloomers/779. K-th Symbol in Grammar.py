class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # count = 0
        # def help(n,k,count):
        #     if n == 1:
        #         return count

        #     leng = 2 ** (n - 1)
        #     prev = 2 ** (n - 2)

        #     if k <= prev:
        #         return help(n - 1, k, count)
        #     else:
        #         count += 1
        #         return help(n - 1, k - prev,count)
        
        # ans = help(n,k,count)
        # if ans % 2 == 0:
        #     return 0
        # else:
        #     return 1
        if n == 1:
            return 0
        
        leng = 2 ** (n - 1)
        prev = 2 ** (n - 2)

        if k <= prev:
            return self.kthGrammar(n - 1, k)
        else:
            return (1 - self.kthGrammar(n - 1, k - prev))