class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return - 1
        def possible(day: int) -> bool:
            count = 0
            bouquets = 0
            for i in bloomDay:
                if i <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets >= m
        low, high = min(bloomDay), max(bloomDay)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1
        return ans