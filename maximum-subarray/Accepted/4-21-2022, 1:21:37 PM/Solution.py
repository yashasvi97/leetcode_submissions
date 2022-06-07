// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        currMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            max_so_far = max(currMax, max_so_far)
        return max_so_far