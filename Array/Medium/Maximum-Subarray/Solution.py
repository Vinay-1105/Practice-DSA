class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = nums[0]
        # current_sum = nums[0]

        # for num in nums[1:]:
        #     current_sum = max(num, current_sum + num)
        #     max_sum = max(max_sum, current_sum)
        # return max_sum
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum