class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(' ')
        if len(words)!=len(pattern):
            return False
        hashmap={}
        seen=set()

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if words[i] in seen:
                    return False
                else:
                    hashmap[pattern[i]]=words[i]
                    seen.add(words[i])
            elif hashmap[pattern[i]]!=words[i]:
                return False
        return True