from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_char = sorted(count, key = count.get, reverse = True)
        ans = ''
        for ch in sorted_char:
            ans += ch * count[ch]
        return ans
