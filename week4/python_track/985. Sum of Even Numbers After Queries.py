class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        queries_len = len(queries)
        even_sum = 0
        ans = []
        for i in nums:
            if i % 2 == 0:
                even_sum += i

        for i in range(queries_len):
            old_value = nums[queries[i][1]]
            value = queries[i][0]

            if old_value % 2 != 0:
                new_value = old_value + value
                if new_value % 2 == 0:
                    even_sum += new_value
                    nums[queries[i][1]] = new_value
                    ans.append(even_sum)
                
                else:
                    ans.append(even_sum)
                    nums[queries[i][1]] = new_value
            
            else:
                even_sum -= old_value
                new_value = old_value + value

                if new_value % 2 == 0:
                    even_sum += new_value
                    nums[queries[i][1]] = new_value
                    ans.append(even_sum)
                
                else:
                    ans.append(even_sum)
                    nums[queries[i][1]] = new_value
        
        return ans





