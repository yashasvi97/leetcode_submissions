// https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i]
        j = n-1
        for i in range(n):
            s += mat[i][j-i]
        if n %2 == 1:
            k = n//2
            s -= mat[k][k]
        return s