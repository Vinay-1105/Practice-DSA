class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        res=""
        for ch in s:
            if ch == "(":
                if cnt>0:
                    res+=ch
                cnt+=1

            elif ch == ")":
                cnt-=1
                if cnt>0:
                    res+=ch
        return res                   