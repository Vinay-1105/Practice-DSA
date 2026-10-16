class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        word=len(words)
        for i in range(word):
            if x in words[i]:
                ans.append(i)
        return ans