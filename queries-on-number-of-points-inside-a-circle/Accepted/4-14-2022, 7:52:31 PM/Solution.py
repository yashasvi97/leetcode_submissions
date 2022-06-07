// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        arr = [0 for i in range(len(queries))]
        k = 0
        for q in queries:
            x_i = q[0]
            y_i = q[1]
            r_i = q[2]
            for p in points:
                x_j = p[0]
                y_j = p[1]
                if (x_i - x_j)**2 + (y_i - y_j)**2 <= r_i**2:
                    arr[k] += 1
            k += 1
        return arr