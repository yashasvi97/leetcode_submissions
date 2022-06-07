// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1 or k > n:
            return
        tmp = nums[-k:]
        c = 0
        for x in range(n-k-1, -1, -1):
            nums[n-1 - c] = nums[x]
            c += 1
        for x in range(0, k):
            nums[x] = tmp[x]