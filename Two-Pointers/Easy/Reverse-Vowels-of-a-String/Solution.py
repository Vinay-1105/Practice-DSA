class Solution:
    def reverseVowels(self, s: str) -> str:
        seen = set("aeiouAEIOU")
        s=list(s)
        l=0
        r=len(s)-1
        while l < r:
            while l<r and s[l] not in seen:
                l += 1
            while l<r and s[r] not in seen:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        return ''.join(s)