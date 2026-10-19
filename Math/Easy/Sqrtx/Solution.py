class Solution:
    def mySqrt(self, x: int) -> int:
        # if x < 2:
        #     return x
        # low=1
        # high = x//2
        # while low <= high:
        #     mid = (low + high) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return high
        if x<2:
            return x
        i=2
        while i*i<=x:
            i+=1
        return i-1