class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, img1 = num1.split("+")
        real2, img2 = num2.split("+")
        
        real1, real2 = int(real1), int(real2)
        img1, img2 = int(img1[ : -1]), int(img2[ : -1])

        ansReal = (real1 * real2) - (img1 * img2)
        ansImg = (real1 * img2) + (img1 * real2)
        ans = str(ansReal) + "+" + str(ansImg) + "i"
        return ans
