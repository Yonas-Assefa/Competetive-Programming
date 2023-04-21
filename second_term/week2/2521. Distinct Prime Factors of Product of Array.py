class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # prod = 1
        # for i in nums:
        #     prod *= i
        # prime = 2

        primeFactors = set()
        for i in nums:
            prod = i
            prime = 2
            while prime * prime <= prod:
                
                while  prod % prime == 0:
                    prod = prod // prime
                    primeFactors.add(prime)

                prime += 1

            if prod > 1:
                primeFactors.add(prod)
            # print(primeFactors)
       
        return len(primeFactors)            

                