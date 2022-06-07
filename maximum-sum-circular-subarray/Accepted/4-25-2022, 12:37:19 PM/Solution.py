// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_so_far = arr[0]
            currMax = arr[0]
            for i in range(1, len(arr)):
                currMax = max(arr[i], currMax + arr[i])
                max_so_far = max(currMax, max_so_far)
            return max_so_far
        mx1 = kadane(nums)
        neg_nums = [-1*x for x in nums]
        mx2 = kadane(neg_nums)
        max_wrap = -(sum(neg_nums)-mx2)
        res = max([mx1, max_wrap])
        if res != 0:
            return res
        else:
            return mx1