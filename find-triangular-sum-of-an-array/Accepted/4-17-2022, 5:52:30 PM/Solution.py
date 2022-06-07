// https://leetcode.com/problems/find-triangular-sum-of-an-array

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) != 1:
            vec = [0 for _ in range(len(nums)-1)]
            for i in range(len(nums)-1):
                vec[i] = (nums[i]+nums[i+1])%10
            nums = vec
        return nums[0]