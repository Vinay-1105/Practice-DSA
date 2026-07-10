class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left=0
        right=0
        max_profit=0
        while right<len(prices):
            current_profit=prices[right]-prices[left]
            if prices[left]<prices[right]:
                max_profit=max(current_profit, max_profit)
            else:
                left=right
            right+=1
        return max_profit
        