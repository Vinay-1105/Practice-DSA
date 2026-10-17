class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={')':'(','}':'{',']':'['}
        stack=[]
        for ch in s:
            if ch not in hashMap:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped != hashMap[ch]:
                        return False
        return not stack 