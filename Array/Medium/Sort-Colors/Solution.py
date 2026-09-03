class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force approach
        # First we will check how 0's, 1's and 2's are present in the array 
        # And based on that we will fill the array first with 0's, then 1's and lastly 2's 
        # basically overwriting in it
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        
        idx = 0
        for _ in range(cnt0):
            nums[idx] = 0
            idx += 1
        for _ in range(cnt1):
            nums[idx] = 1
            idx += 1
        for _ in range(cnt2):
            nums[idx] = 2
            idx += 1