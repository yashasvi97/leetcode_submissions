// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min([cost[0], cost[1]])
        else:
            
            local = [0] * (n+1)
            local[0] = 0
            local[1] = 0
            local[2] = min([cost[0], cost[1]])
            for i in range(3, n+1):
                local[i] = min([cost[i-1]+local[i-1], cost[i-2]+local[i-2]])
            return local[n]