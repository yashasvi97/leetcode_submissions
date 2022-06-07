// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_so_far = nums[0]
        # currMax = nums[0]
        # for i in range(1, len(nums)):
        #     currMax = max(nums[i], currMax + nums[i])
        #     max_so_far = max(currMax, max_so_far)
        # return max_so_far
        
        def max_cross(arr, l, m, h):
            sm = 0
            left_sum = -10000
            for i in range(m, l-1, -1):
                sm += arr[i]
                if sm > left_sum:
                    left_sum = sm
            
            sm = 0
            right_sum = -10000
            for i in range(m+1, h+1):
                sm += arr[i]
                if sm > right_sum:
                    right_sum = sm
            
            return max([left_sum+right_sum, left_sum, right_sum])
        
        def max_sub_arr_util(arr, l, h):
            if l == h:
                return arr[l]
            m = (l+h)//2
            return max([max_sub_arr_util(arr, l, m), max_sub_arr_util(arr, m+1, h), max_cross(arr, l, m, h)])
        
                       
        return max_sub_arr_util(nums, 0, len(nums)-1)