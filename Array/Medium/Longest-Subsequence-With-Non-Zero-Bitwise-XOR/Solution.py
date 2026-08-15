from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor_val = 0
        non_zero = False
        for x in nums:
            xor_val ^= x

            if x != 0:
                non_zero = True
        if xor_val != 0:
            return n
        if non_zero:
            return n - 1
        return 0