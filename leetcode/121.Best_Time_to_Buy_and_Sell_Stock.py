class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prf = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            prf = max(profit,prf)
        return prf
