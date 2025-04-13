class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # Start from index 1, since first element is always unique
        
        for i in range(1, len(nums)):
           # For every element starting from index 1, if it is not equal to the previous unique element, we write it to index k and increment k.
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
        