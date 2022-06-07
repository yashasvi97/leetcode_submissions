// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        myCache = {0: 0, 1: 1, 2: 1}
        def trib_util(n):
            if n in myCache:
                return myCache[n]
            myCache[n] = trib_util(n-3) + trib_util(n-2) + trib_util(n-1)
            return myCache[n]
        return trib_util(n)