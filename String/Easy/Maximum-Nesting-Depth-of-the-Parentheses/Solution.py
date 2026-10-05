class Solution:
    def maxDepth(self, s: str) -> int:
        # Basically, we have to check how my maximum open brackets are there or it reaches
        # If one bracket opens cnt = 1, 
        # after that if one more open bracket
        # cnt = 2, if we find a close bracket
        # cnt -= 1 and so on.
        result=0
        cnt=0
        for ch in s:
            if ch == "(":
                cnt+=1
            elif ch == ")":
                cnt-=1
            result = max(result, cnt)
        return result