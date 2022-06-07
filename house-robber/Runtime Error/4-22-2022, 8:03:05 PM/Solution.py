// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        else:
            n = len(nums)
            local = [0] * (n+1)
            local[0] = 0
            local[1] = nums[0]
            local[2] = max([nums[0], nums[1]])
            for i in range(3, n+1):
                local[i] = max(nums[i-1]+local[i-2], local[i-1])
            return local[n]