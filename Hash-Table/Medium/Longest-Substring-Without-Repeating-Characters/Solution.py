class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        l=0
        res={}

        for r, ch in enumerate(s):
            if ch in res and res[ch] >= l:
                l=res[ch]+1
            max_len=max(max_len, r-l+1)
            res[ch]=r
        return max_len