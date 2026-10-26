class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        n=len(nums)
        k=0
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k]=nums[i]
                k+=1
        return k
        # # Optimal approach
        # n = len(nums)
        # i = 0
        # for j in range(1,n):
        #     if nums[i] != nums[j]:
        #         i+=1
        #         nums[i] = nums[j]
        # return len(nums[:i+1])