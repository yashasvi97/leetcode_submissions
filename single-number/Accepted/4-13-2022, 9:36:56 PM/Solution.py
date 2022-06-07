// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        for k in d:
            if d[k] == 1:
                return k