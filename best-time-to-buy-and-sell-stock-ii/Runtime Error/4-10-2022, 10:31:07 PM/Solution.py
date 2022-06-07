// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        s = 0
        i = 0
        while i < n-1:
            if prices[i] < prices[i+1]:
                j = i+1
                while j < n and prices[j] > prices[i]:
                    if prices[j] > prices[j+1]:
                        break
                    j += 1
                if j == n:
                    break
                if j > i:
                    s += prices[j] - prices[i]
                    i = j+1
            else:
                i += 1
        return s