class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Brute Force Approach
        positive = []
        negative = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        i = 0
        while 2 * i < len(nums):
            nums[2 * i] = positive[i] # For alternate signs +,-,+,-,+,-
            nums[2 * i + 1] = negative[i] # For alternate signs +,-,+,-,+,-
            i += 1
        return nums
