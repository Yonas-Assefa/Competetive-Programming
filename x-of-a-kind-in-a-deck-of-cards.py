class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count = Counter(deck)
        uniqueCard = list(count.values())
        uniqueCard.sort()
        if len(uniqueCard) == 1:
            for i in uniqueCard:
                if i != 1:
                    return True
            return False
        a = 0
        b = 1
        while b < len(uniqueCard) and uniqueCard[a] == uniqueCard[b]:
            a += 1
            b += 1
        if b == len(uniqueCard):
            return True 
        base = self.gcd(uniqueCard[a], uniqueCard[b])
        if base == 1:
            return False
        print(base)
        print(uniqueCard)
        for i in range(1, len(uniqueCard)):
            if uniqueCard[i] % base != 0:
                return False
        return True

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def factor(self, num):
        init = 2
        while num > 2 and num % init == 0:

            while num > 2 and num % init == 0:
                num //= init

            init += 1

        return  num