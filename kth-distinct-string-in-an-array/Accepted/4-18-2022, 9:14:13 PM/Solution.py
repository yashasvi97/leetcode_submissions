// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # from collections import OrderedDict
        d = {}
        for s in arr:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        for s in arr:
            if d[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
        