// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False