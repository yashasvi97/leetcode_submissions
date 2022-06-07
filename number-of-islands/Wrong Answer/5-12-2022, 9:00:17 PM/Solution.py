// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        visit = [[False for c in range(COLS)] for r in range(ROWS)]
        
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0 or
                visit[r][c]):
                return
            
            visit[r][c] = True
            
            # island.add((r, c))
            
            i1 = dfs(r+1, c)
            # if i1 is not None:
                # island = i1
            i2 = dfs(r-1, c)
            # if i2 is not None:
                # island = i2
            i3 = dfs(r, c+1)
            # if i3 is not None:
                # island = i3
            i4 = dfs(r, c-1)
            # if i4 is not None:
                # island = i4
            
            return 1
        
        k = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not visit[r][c] and grid[r][c]:
                    res = dfs(r, c)
                    if res is not None:
                        k += 1
                    
        return k