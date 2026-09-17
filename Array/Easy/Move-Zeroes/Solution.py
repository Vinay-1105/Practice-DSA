class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == 0:
        #             temp = nums[j]
        #             nums[j] = nums[i]
        #             nums[i] = temp

        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left] = nums[right]
                left+=1
        while left < n:
            nums[left] = 0
            left+=1