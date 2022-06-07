// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        def getPascalRow(n):
            t = [0]*(n+1)
            t[0] = 1
            for i in range(n+1):
                for j in range(i, 0, -1):
                    t[j] += t[j-1]
            return t
            
        for i in range(numRows):
            r = getPascalRow(i)
            ans.append(r)
        return ans