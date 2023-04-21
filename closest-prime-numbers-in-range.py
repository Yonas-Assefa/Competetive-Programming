class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primeNumbers = []
        ans = [-1,-1]
        maxLen = float("inf")
        for i in range(left, right + 1):
            if self.isPrime(i):
                primeNumbers.append(i)
                if len(primeNumbers) >= 2:
                    diff = primeNumbers[-1] - primeNumbers[-2]
                    if diff < maxLen:
                        maxLen = diff
                        ans = [primeNumbers[-2], primeNumbers[-1]]
            if maxLen <= 2:
                break
        print(primeNumbers, i)

       
        return ans
    
    def isPrime(self, num):
        if num < 2:
            return False
        
        prime = 2
        while prime ** 2 <= num:
            if num % prime == 0:
                return False
            prime += 1
        print(num, "prime")
        return True
        
        # primes = [True for _ in range(right + 1)]
        # primes[0] = primes[1] = False
        # prime = 2

        # while prime * prime <= right:
        #     nxt = prime * 2
        #     while nxt <= right:
        #         primes[nxt] = False
        #         nxt += prime
        #     prime += 1
        # temp = []
        # # print(primes)
        # for i in range(left, right + 1):
        #     if primes[i]:
        #         temp.append(i)
        # minLen = len(primes)
        # ans = []
        # # print(temp)
        # for j in range(1, len(temp)):
        #     leng = temp[j]  - temp[j - 1]
        #     if leng < minLen:
        #         ans = [temp[j - 1], temp[j]]
        #         minLen = leng
        #     if minLen <= 2:
        #         break
        # if ans:
        #     return ans
        # return [-1, -1]