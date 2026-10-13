class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # pehle alphanumeric characters ko extract
        # # fir resulting string ko lower case mai convert 
        # # lastly, reversing the string and compare with the original string
        res=""
        for ch in s:
            if ch.isalnum():
                res+=ch

        res=res.lower()
        if res==res[::-1]:
            return True
        return False      