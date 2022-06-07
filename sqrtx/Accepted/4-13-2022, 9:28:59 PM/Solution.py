// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        y = 1
        while y*y <= x:
            y += 1
        return y-1