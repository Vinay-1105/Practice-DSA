class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        res=0

        if not s:
            return 0

        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign=-1
            s=s[1:]

        for ch in s:
            if not ch.isdigit():
                break
            res=res*10+int(ch)
        res=res*sign

        if res < -2**31:
            return -2**31
        elif res > 2**31-1:
            return 2**31-1
        
        return res