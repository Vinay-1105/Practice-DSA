class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # pehle alphanumeric characters ko extract
        # # fir resulting string ko lower case mai convert 
        # # lastly, reversing the string and compare with the original string
        # ans=""
        # for i in s:
        #     if i.isalnum():
        #         ans+=i
        # ans=ans.lower()
        # if ans==ans[::-1]:
        #     return True
        # return False

        # Using two-pointer;
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True