class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pehle alphanumeric characters ko extract
        # fir resulting string ko lower case mai convert 
        # lastly, reversing the string and compare with the original string
        ans=""
        for i in s:
            if i.isalnum():
                ans+=i
        ans=ans.lower()
        if ans==ans[::-1]:
            return True
        return False