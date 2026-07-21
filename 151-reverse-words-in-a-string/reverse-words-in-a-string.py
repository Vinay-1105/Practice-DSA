class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # return " ".join(words[::-1])

        return " ".join(reversed(s.split()))