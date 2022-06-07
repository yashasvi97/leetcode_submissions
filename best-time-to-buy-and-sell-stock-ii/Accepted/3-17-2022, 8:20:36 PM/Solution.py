// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        tot_sum = 0
        edge = 0
        n = len(prices)
        while 1:
            while i < n-1 and prices[i] > prices[i+1]:
                i += 1
            if i == n:
                edge = 1
                break
            j = i
            while j < n-1 and prices[j] < prices[j+1]:
                j += 1
            if j == n:
                edge = 1
                tot_sum += abs(prices[j] - prices[i])
                break
            tot_sum += abs(prices[j]-prices[i])
            i = j + 1
        return tot_sum