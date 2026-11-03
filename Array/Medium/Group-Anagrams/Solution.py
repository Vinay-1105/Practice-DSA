from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict=defaultdict(list)
        for s in strs:
            cnt=[0]*26
            for c in s:
                cnt[ord(c)-ord('a')]+=1
            key=tuple(cnt)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())