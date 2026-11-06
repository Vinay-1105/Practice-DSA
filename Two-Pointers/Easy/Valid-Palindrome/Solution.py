class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for ch in s:
            if ch.isalnum():
                res+=ch
        res=res.lower()
        if res==res[::-1]:
            return True
        return False            