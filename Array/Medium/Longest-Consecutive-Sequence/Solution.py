class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest = 0
        # num_set = set(nums)

        # for n in num_set:
        #     if (n-1) not in num_set:
        #         length = 1
        #         while (n+length) in num_set:
        #             length += 1
        #         longest = max(longest, length)
        
        # return longest
        longest = 0
        seen=set(nums)
        for n in seen:
            if n-1 not in seen:
                len=1
                while n+len in seen:
                    len+=1
                longest=max(longest, len)
        return longest