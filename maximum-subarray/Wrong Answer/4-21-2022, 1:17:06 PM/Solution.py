// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = 0
        for x in nums:
            max_ending_here = max_ending_here + x
            if max_ending_here < 0:
                max_ending_here = 0
            elif max_so_far < max_ending_here:
                max_so_far = max_ending_here
            
        return max_so_far