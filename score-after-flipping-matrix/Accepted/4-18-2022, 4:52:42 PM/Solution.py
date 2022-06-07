// https://leetcode.com/problems/score-after-flipping-matrix

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        for r in grid:
            tmp = r.copy()
            tmp = [1-x for x in tmp]
            tmp_str = ''.join([str(_) for _ in tmp])
            r_str   = ''.join([str(_) for _ in r])
            if int(tmp_str, 2) > int(r_str, 2):
                for idx, _ in enumerate(tmp):
                    r[idx] = tmp[idx]
        
        for c in range(m):
            c_zero = 0
            c_one = 0
            for i in range(n):
                if grid[i][c] == 1:
                    c_one += 1
                elif grid[i][c] == 0:
                    c_zero += 1
                
            if c_one < c_zero:
                for i in range(n):
                    grid[i][c] = 1-grid[i][c]
        # print(grid)
        s = 0
        for r in grid:
            s += int(''.join([str(_) for _ in r]), 2)
        return s