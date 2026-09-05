class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we have an array of prices for stocks
        # Each day the stock changes
        # we can buy a stock and sell it later
        # array can only be traversed once

        # we need to come up with a function and a max of the function to get max profit
        # the function will calculate the maximum profit and we return that

        # f(x) = max(f(x-1), f(x))

        # We can find the minimum on the left and the maximum on the right
        # profit = 0
        # l = 0 
        # n = len(prices)
        # r = 1
        # profit = 0
        # while (r < n):
        #     profit = max(profit, (prices[r] - prices[l]))
        #     if(prices[r] < prices[l]):
        #         l = r
        #     r+=1
        # return profit

        max_profit = 0
        highest = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            if profit > max_profit:
                max_profit = profit

        return max_profit
            