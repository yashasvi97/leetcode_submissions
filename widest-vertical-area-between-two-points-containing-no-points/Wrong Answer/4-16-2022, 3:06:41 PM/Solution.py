// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        left_to_right = sorted(points, key=lambda x: x[0])
        i = 0
        j = i+1
        p1 = left_to_right[i]
        p2 = left_to_right[j]
        area = 0
        if p2[0] - p1[0] > 0:
            area = p2[0] - p1[0]
        i = j+1
        j = i+1
        while i <= n-2:
            p1 = left_to_right[i]
            p2 = left_to_right[j]
            if p1[0] == p2[0]:
                i = i+1
                j = i+1
            else:
                tmp_area = p2[0] - p1[0]
                if tmp_area > area:
                    area = tmp_area
                i = j+1
                j = i+1
        return area