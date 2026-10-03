class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        for ch in s:
            if ch in hashMap:
                hashMap[ch] += 1
            else:
                hashMap[ch] = 1
        for ch in range(len(s)):
            if hashMap[s[ch]] == 1:
                return ch
        return -1
        