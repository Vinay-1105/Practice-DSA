class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum_div(d):
            return sum((i + d - 1) // d for i in nums)
        n = len(nums)
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if sum_div(mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low