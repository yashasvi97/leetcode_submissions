// https://leetcode.com/problems/maximum-number-of-coins-you-can-get

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        b = 0
        a = len(piles)-1
        s = 0
        while len(piles) > 0:
            s += piles[a-1]
            piles.pop(a)
            piles.pop(a-1)
            piles.pop(b)
            a = len(piles)-1
            b = 0
        return s