class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0: # Condition to check for odd number
                return num[: i + 1]
        return "" # Return "" if no odd number exists