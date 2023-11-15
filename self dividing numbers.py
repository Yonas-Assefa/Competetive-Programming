class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            strNum = str(num)
            leng = len(strNum)

            if "0" not in strNum:
                flag = False
                for digit in strNum:
                    if num % (int(digit)) != 0:
                        flag = True
                        break
                
                if not flag:
                    ans.append(num)
        return ans


        
