class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # right pointer to iterate through each characters..
        # left pointer to store values in hashmap
        max_length=0
        left=0
        res={}
        for right, ch in enumerate(s):
            if ch in res and res[ch]>=left:
                left=res[ch]+1
            max_length=max(max_length, right-left+1)
            res[ch]=right
        return max_length