class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        outside_exponent = 0
        ans = 0
        for i in range(len1 - 1, -1, -1):
            current_product = 0
            oprand1 = ord(num1[i]) - ord("0")
            exponent = 0
            for j in range(len2 - 1,-1,-1):
                oprand2 = ord(num2[j]) - ord("0")
                current_product += ((oprand1 * oprand2)*(10 ** exponent))
                exponent += 1
            ans += current_product *(10 ** outside_exponent)
            outside_exponent += 1
        return str(ans)
