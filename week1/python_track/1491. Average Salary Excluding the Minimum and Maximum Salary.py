class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) == 2:
            return 0
        salary.sort()
        salary_len = len(salary)
        salary_sum = sum(salary[1:salary_len - 1])
        print(salary_sum)
        return salary_sum / (salary_len - 2)