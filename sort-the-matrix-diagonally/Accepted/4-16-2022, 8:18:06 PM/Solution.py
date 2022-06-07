// https://leetcode.com/problems/sort-the-matrix-diagonally

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        i = n-2
        while i >= 0:
            x = i; y = 0;
            arr = []
            p = 0
            while x+p < n and y+p < m:
                arr.append(mat[x+p][y+p])
                p += 1
            arr.sort()
            p=0
            while x+p < n and y+p < m:
                mat[x+p][y+p] = arr[p]
                p += 1
            i -= 1
        
        j = 1
        while j < m:
            x = 0; y = j;
            arr = []
            p = 0
            while x+p < n and y+p < m:
                arr.append(mat[x+p][y+p])
                p += 1
            arr.sort()
            p = 0
            while x+p < n and y+p < m:
                mat[x+p][y+p] = arr[p]
                p += 1
            j += 1
        
        return mat