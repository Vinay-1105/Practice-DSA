import math
class Solution:
    def sumByD(self, nums, d):
        return sum(math.ceil(i / d) for i in nums) 
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n > threshold:
            return -1
        
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low
