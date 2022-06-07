// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        tmp = [0 for _ in range(k)]
        j = n-1; i = j-k
        x = k-1
        while x >= 0:
            tmp[x] = nums[j]
            x -= 1; j -= 1
        ctr = 0
        while ctr < k:
            nums[n-1-ctr] = nums[i-ctr]
            nums[i-ctr] = nums[i-k-ctr]
            ctr = ctr + 1
        # moving done
        for ctr in range(0, k):
            nums[ctr] = tmp[ctr]