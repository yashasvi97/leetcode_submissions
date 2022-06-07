// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            def hr_helper(arr):
                n = len(arr)
                local = [0] * n
                local[0] = arr[0]
                local[1] = max([arr[0], arr[1]])
                for i in range(2, n):
                    local[i] = max(arr[i]+local[i-2], local[i-1])
                return local[n-1]
            mx1 = hr_helper(nums[:-1])
            mx2 = hr_helper(nums[1:])
            return max([mx1, mx2])