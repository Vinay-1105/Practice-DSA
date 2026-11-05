class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        res=high
        while low<=high:
            mid=(low+high)//2
            total_hrs=sum((p+mid-1)//mid for p in piles)
            if total_hrs<=h:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res