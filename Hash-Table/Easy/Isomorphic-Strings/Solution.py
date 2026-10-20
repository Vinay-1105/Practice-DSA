class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for idx in s:
            s1.append(s.index(idx))
        for idx in t:
            s2.append(t.index(idx))
        if s1==s2:
            return True
        return False