class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import defaultdict

        no_meals = len(deliciousness)
        good_meal = 0
        count = defaultdict(int)

        for meal in deliciousness:
            for i in range(22):
                target = (2**i) - meal
                good_meal += count[target]
            count[meal] += 1

        good_meal_modulo = good_meal % (1000000007)
        
        return good_meal_modulo
                

