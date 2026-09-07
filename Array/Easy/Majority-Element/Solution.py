class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute Force Approach
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[j] == nums[i]:
        #             count += 1
        #         if count > (n // 2):
        #             return nums[i]
        # return -1

        # Optimal Solution 
        cnt = 0
        el = 0
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
        cnt1 = nums.count(el)
        if cnt1 > (len(nums) // 2):
            return el
        return -1