def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for i in range(1, n):
        min_price = min(min_price, prices[i])   # updating the minimum price
        possible_profit = prices[i] - min_price # possible profits by subtracting minimum price
        max_profit = max(max_profit, possible_profit) #finding max profit possible

    return max_profit

prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))

"""
Question4: Buy or Sell stock to make maximum benefits

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

