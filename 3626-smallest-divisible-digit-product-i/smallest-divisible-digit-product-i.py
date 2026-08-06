class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n
        while True:
            product = 1
            temp = current
            while temp > 0:
                product *= temp % 10
                temp = temp // 10
            if product % t == 0:
                return current
            current += 1