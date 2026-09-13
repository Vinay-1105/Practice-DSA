class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen = set()
        # cnt = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #         nums[cnt] = nums[i]
        #         cnt += 1
        # return cnt

        if not nums:
            return 0
        n = len(nums)
        i = 0
        for j in range(1, n):
            if nums[i] != nums[j]:
               i += 1
               nums[i] = nums[j]
        return i+1