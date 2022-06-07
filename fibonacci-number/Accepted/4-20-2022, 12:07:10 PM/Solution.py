// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        myCache = {0: 0, 1: 1}
        def fib_util(n):
            if n in myCache:
                return myCache[n]
            myCache[n] = fib_util(n-1) + fib_util(n-2)
            return myCache[n]
        return fib_util(n)