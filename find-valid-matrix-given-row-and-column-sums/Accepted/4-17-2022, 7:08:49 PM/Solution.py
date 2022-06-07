// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        mat = []
        for i in range(n): 
            r = [0 for j in range(m)]
            mat.append(r)
        # print(mat)
        for i in range(n):
            for j in range(m):
                r_i = rowSum[i]
                c_j = colSum[j]
                x = min(r_i, c_j)
                # print(type(x))
                mat[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x
        return mat