// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            local = [0]* (n+1)
            local[0] = 0
            local[1] = 1
            local[2] = 2
            for i in range(3, n+1):
                local[i] = local[i-1] + local[i-2]

            return local[n]