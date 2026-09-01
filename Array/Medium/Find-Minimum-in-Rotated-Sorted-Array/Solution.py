class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[0]
        n = len(nums)
        low = 0
        high = n-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        return nums[low]               