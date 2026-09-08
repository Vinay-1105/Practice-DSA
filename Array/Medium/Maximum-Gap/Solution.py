class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        counter = 0
        for i in range(n-1):
            counter = max(counter,nums[i+1]-nums[i])
        return counter