// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        i = 0
        n = len(nums)
        while i < n and i <= reach:
            reach = max([i + nums[i], reach])
            i += 1
        return i == n