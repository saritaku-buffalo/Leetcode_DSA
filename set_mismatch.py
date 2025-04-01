class Solution:
    def findErrorNums(self, nums):
       total_sum = sum(nums)
       set_sum = sum(set(nums)) 
       n = len(nums)
       expected_sum = n * (n+1) // 2
       duplicate = total_sum - set_sum
       missing = expected_sum - set_sum
       return [duplicate, missing]
        