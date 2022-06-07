// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k > 0:
            # i = n-k
            j = n-1
            # tmpk = nums[i]
            tmpn = nums[j]
            while j > 0:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = tmpn
            k -= 1
            