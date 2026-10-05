class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        l,r = 0 , 1
        while r < len(prices):
            selling = prices[r] - prices[l]
            if selling > profit: 
                profit = selling 
            if prices[l] > prices[r]:
                l = r
            r += 1
        return profit