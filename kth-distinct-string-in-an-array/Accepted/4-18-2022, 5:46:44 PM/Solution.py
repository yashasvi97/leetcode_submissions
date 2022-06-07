// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import OrderedDict
        d = OrderedDict()
        for s in arr:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        d_keys = list(d.keys())
        for key in d_keys:
            if d[key] > 1:
                d.pop(key)
        if k > len(d.keys()):
            return ""
        else:
            x = 0
            for key in d:
                x += 1
                if x == k:
                    return key
            