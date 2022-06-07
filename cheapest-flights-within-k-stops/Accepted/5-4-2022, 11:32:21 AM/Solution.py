// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import sys
        INF = sys.maxsize
        # make graph
        g = {}
        for i in range(n):
            g[i] = {}
        for (f, t, p) in flights:
            g[f][t] = p
        
        # construct DP array
        costs = []
        for i in range(n):
            tmp = [-1]* (k+1)
            costs.append(tmp)
        
        
        # helper function to traverse the tree
        def dfs(root, steps):
            if steps == k+1 and root != dst:
                return INF
            if root == dst:
                return 0
            if costs[root][steps] != -1:
                return costs[root][steps]
            
            min_cost = INF
            for u in g[root]:
                min_cost = min(min_cost, g[root][u] + dfs(u, steps+1) )
            
            costs[root][steps] = min_cost
            return min_cost
        
        ans = dfs(src, 0)
        #=======================================================
        # assuming costs is filled with best costs from u to dst with at most x steps
        if ans == INF:
            return -1
        else:
            return ans