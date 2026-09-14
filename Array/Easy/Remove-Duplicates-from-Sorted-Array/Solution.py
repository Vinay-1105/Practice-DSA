class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1
        return k