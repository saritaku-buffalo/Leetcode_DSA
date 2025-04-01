class Solution:
    def thirdMax(self, nums):
        uniquenum = list(set(nums))
        uniquenum.sort(reverse=True)
        if len(uniquenum) >= 3:
            return uniquenum[2]
        else:
            return uniquenum[0]