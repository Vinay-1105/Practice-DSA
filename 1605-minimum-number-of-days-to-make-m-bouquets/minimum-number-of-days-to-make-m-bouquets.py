class Solution:
    def is_possible(self, bloomDay, day, m, k):
        count = 0
        bouquets = 0
        for b in bloomDay:
            if b <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0

        return bouquets >= m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        res = -1

        while low <= high:
            mid = (low + high) // 2
            if self.is_possible(bloomDay, mid, m, k):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res