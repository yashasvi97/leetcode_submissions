// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        reach = 0
        last_reach = 0
        i = 0
        n = len(nums)
        steps = 0
        while i< n and i<= reach:
            if i > last_reach:
                steps += 1
                last_reach = reach
            reach = max([i + nums[i], reach])
            i += 1
        if reach < len(nums) - 1:
            return 0
        return steps