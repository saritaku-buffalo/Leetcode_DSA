def Two_sum(nums, target):
    num_map = {}
    for i, num in enumerate (nums):
        complement = target - num
        if complement in num_map:
            print (num_map[complement], i)
        num_map[num] = i
    return []