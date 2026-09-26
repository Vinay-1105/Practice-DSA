class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 0
        seen=set(nums)
        for n in seen:
            if n-1 not in seen:
                len=1
                while n+len in seen:
                    len+=1
                longest=max(longest, len)
        return longest