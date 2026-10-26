class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left]=nums[right]
                left+=1
        while left<len(nums):
            nums[left]=0
            left+=1
        # temp=0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==0:
        #             temp=nums[j]
        #             nums[j]=nums[i]
        #             nums[i]