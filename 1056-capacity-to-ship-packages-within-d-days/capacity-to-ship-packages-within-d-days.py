class Solution:
    def DaysNeeded(self, weights, capacity):
        days = 1
        currentLoad = 0
        for i in weights:
            if currentLoad + i > capacity:
                days += 1
                currentLoad = i
            else:
                currentLoad += i
        return days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            needed = self.DaysNeeded(weights, mid)
            if needed <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low