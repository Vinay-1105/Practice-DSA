class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[cnt] = nums[i]
                cnt += 1
        return cnt