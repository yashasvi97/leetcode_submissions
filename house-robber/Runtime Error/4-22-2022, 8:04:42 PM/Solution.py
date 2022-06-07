// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        else:
            n = len(nums)
            local = [0] * (n+1)
            local[0] = nums[0]
            local[1] = max([nums[0], nums[1]])
            
            for i in range(2, n):
                local[i] = max(nums[i]+local[i-2], local[i-1])
            return local[n-1]