// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        dup = 0
        for i in range(n-1):
            j = i + 1
            while j <= n-1 and nums[j] == nums[i]:
                dup = 1
                j += 1
            if dup == 1:
                if j == n:
                    break
                num_dup = (j-i-1)
                for x in range(j, n):
                    nums[x-num_dup] = nums[x]
                    n -= num_dup
                    nums[n] = -101
                dup = 0
            else:
                continue
        if dup == 1:
            num_dup = (j-i-1)
            for x in range(j, n):
                nums[x-num_dup] = nums[x]
                n -= num_dup
                nums[n] = -101
            dup = 0
        return n