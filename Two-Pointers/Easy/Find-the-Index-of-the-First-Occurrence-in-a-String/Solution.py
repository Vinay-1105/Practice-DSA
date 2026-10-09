class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # brute force approach using nested loops
        # if needle=="":
        #     return 0
        
        # for i in range(len(haystack)+1-len(needle)):
        #     for j in range(len(needle)):
        #         if haystack[i+j] != needle[j]:
        #             break
        #         if j==len(needle)-1:
        #             return i
        # return -1

        if needle=="":
            return 0
        for i in range(len(haystack)+1-len(needle)):
            if haystack[i: i+len(needle)]==needle:
                return i
        return -1