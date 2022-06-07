// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr = [0 for i in range(len(nums))]
        sum_arr[0] = nums[0]
        for i in range(1, len(nums)):
            sum_arr[i] = sum_arr[i-1] + nums[i]
        return sum_arr