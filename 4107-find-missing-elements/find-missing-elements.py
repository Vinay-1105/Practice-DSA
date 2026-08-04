class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        mn = min(nums)
        mx = max(nums)

        result = []
        for i in range(mn, mx + 1):
            if i not in seen:
                result.append(i)
        return result        