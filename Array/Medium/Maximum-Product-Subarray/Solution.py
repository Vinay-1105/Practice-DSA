class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        max_prod=float('-inf')
        prefix=1
        suffix=1

        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix *= nums[i]
            suffix *= nums[n-i-1]
            max_prod=max(max_prod, prefix, suffix)
        return max_prod