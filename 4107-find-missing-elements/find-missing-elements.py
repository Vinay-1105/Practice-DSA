class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        mn = min(nums)
        mx = max(nums)
        res = []

        for i in range(mn, mx + 1):
            if i not in seen:
                res.append(i)
        return res