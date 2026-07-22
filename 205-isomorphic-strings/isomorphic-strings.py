class Solution(object):
    def isIsomorphic(self, s, t):
        s1 = []
        s2 = []
        for idx in s:
            s1.append(s.index(idx))
        for idx in t:
            s2.append(t.index(idx))
        if s1 == s2:
            return True
        return False
        