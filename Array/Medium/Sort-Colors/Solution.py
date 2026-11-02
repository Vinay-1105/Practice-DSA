class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # cnt0=0
        # cnt1=0
        # cnt2=0
        # for num in nums:
        #     if num==0:
        #         cnt0+=1
        #     elif num==1:
        #         cnt1+=1
        #     else:
        #         cnt2+=1
        # for i in range(cnt0):
        #     nums[i]=0
        # for i in range(cnt0, cnt0+cnt1):
        #     nums[i]=1
        # for i in range(cnt0+cnt1, n):
        #     nums[i]=2
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[low], nums[mid]=nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid], nums[high]=nums[high], nums[mid]
                high-=1