class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)  
        for i in range(n):
            if ((i == 0 or nums[i - 1] < nums[i]) and (i == n - 1 or nums[i] > nums[i + 1])):
                return i  

        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                high = mid
            else:
                low = mid + 1
        return low 