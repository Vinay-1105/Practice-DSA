class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        mn = min(nums)
        mx = max(nums)

        result = []
        for x in range(mn, mx + 1):
            if x not in seen:
                result.append(x)
        return result        