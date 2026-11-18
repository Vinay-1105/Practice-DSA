class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        # hashmap={}
        # for i,num in enumerate(nums):
        #     complement=target-num
        #     if complement in hashmap:
        #         return [hashmap[complement], i]
        #     hashmap[num]=i
        # return []