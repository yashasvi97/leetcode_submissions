// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def max_sub_array(arr):
            max_so_far = arr[0]
            currMax = arr[0]
            for i in range(1, len(arr)):
                currMax = max(arr[i], currMax + arr[i])
                max_so_far = max(currMax, max_so_far)
            return max_so_far
        mx1 = max_sub_array(nums[:-1])
        mx2 = max_sub_array(nums[1:])
        return max([mx1, mx2])