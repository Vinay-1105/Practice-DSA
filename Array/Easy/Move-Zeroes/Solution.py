class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two-pointers method
        # left pointer is used to represent the position where the next non-zero element
        # should go
        left = 0
        n = len(nums)
        for right in range(n):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        for i in range(left, n):
            nums[i] = 0
