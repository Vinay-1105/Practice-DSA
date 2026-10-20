class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #brute force approach as it taks O(n^2)
        #as index() method searches the string from the beginning each time, which make slower for longer strings.
        # s1=[]
        # s2=[]
        # for idx in s:
        #     s1.append(s.index(idx))
        # for idx in t:
        #     s2.append(t.index(idx))
        # if s1==s2:
        #     return True
        # return False

        hashmap1={}
        hashmap2={}
        for i in range(len(s)):
            if s[i] in hashmap1 and hashmap1[s[i]]!=t[i]:
                return False
            if t[i] in hashmap2 and hashmap2[t[i]]!=s[i]:
                return False    
            hashmap1[s[i]]=t[i]
            hashmap2[t[i]]=s[i]
        return True