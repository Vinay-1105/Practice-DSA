class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)  
        for i in range(n):
            if ((i == 0 or nums[i - 1] < nums[i]) and (i == n - 1 or nums[i] > nums[i + 1])):
                return i  