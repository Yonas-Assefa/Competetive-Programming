class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.n = len(num)

        for i in range(1, self.n):
            for j in range(i + 1, self.n):
                num1 = num[: i]
                num2 = num[i : j]

                if len(num1) != len(str(int(num1))):
                    return False

                if len(num2) != len(str(int(num2))):
                    break

                if self.additiveNumber(int(num1), int(num2), j, num):
                    return True

        return False
            
        
    def additiveNumber(self, num1, num2, j, num):
        if j == self.n:
            return True

        target = num1 + num2
        if num[j : ].startswith(str(target)):
            return self.additiveNumber(num2, target, j + len(str(target)), num)
        
        return False

      

        # def checkAdditive(prev, ind):
        #     if ind == len(num):
        #         print(ind,prev)
        #         return False
        #     if len(prev) != len(str(int(prev))):
        #        return False
        #     prev = int(prev)
        #     print(prev, "next prev")
        #     for j in range(ind, len(num)):
        #         nxt = num[ind: j + 1]
        #         if len(nxt) != len(str(int(nxt))):
        #             break
        #         nxt = int(nxt)
        #         add = prev + nxt
        #         print(add)
        #         add_len = (j + 1) + len(str(add))
        #         if add_len <= len(num):
        #             print((num[j + 1: add_len]),"after qeual")
        #             if str(add) == str(num[j + 1: add_len]):
        #                 print("equal", j + len(str(add)))
        #                 if (j + len(str(add)) + 1) == len(num):
        #                     return True
        #                 return (checkAdditive(str(nxt), j + 1))
                            
                
        #     print("botm", ind, prev)
        #     return False
        # if len(num) <= 2:
        #     return False

        # for i in range(len(num)):
        #     val = num[: i + 1]
        #     print(val,"start")
        #     if checkAdditive(val, i + 1):
        #         return True
        
        # return False
