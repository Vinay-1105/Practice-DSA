class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curr_res = (nums[i]-1) * (nums[j]-1)
                ans=max(ans, curr_res)
        return ans