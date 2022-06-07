// https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        bef = []
        af = []
        bet = []
        for x in nums:
            if x < pivot:
                bef.append(x)
            elif x > pivot:
                af.append(x)
            elif x == pivot:
                bet.append(x)
        fin = bef + bet + af
        return fin