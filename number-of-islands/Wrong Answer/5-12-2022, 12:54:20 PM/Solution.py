// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        islands = {}
        visit = set()
        
        def dfs(r, c, k):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0
            
            visit.add((r, c))
            if dfs(r+1, c, k): visit.add((r+1, c))
            if dfs(r-1, c, k): visit.add((r-1, c))
            if dfs(r, c+1, k): visit.add((r, c+1))
            if dfs(r, c-1, k): visit.add((r, c-1))
            islands[k] = visit
            k += 1
            # visit.remove((r, c))
            
            return k
            
        k = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit:
                    k = dfs(r, c, k)
                
                
        return len(list(islands.keys()))