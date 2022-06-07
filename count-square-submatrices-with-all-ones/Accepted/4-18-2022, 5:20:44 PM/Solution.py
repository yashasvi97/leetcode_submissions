// https://leetcode.com/problems/count-square-submatrices-with-all-ones

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        N = len(matrix)
        M = len(matrix[0])
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][j] == 0:
                    continue
                
                matrix[i][j] = min([matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]]) + 1
        
        c = 0
        for i in range(N):
            for j in range(M):
                c += matrix[i][j]
        
        return c