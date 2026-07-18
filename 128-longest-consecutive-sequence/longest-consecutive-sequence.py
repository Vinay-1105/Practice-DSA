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

        n = len(nums)
        if n == 0:
            return 0
        
        longest = 1
        seen = set()

        for i in range(n):
            seen.add(nums[i])
        for it in seen:
            if it - 1 not in seen:
                cnt = 1
                x = it

                while x + 1 in seen:
                    x += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest