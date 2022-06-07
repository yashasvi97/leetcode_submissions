// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = n
        for i in range(n-1):
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            if j != i+1:
                num_dup = (j-i-1)
                k -= num_dup
                for x in range(j, n):
                    nums[x-num_dup] = nums[x]
                    nums[n-1] = -101
            else:
                continue
        return k