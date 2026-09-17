class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == 0:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp