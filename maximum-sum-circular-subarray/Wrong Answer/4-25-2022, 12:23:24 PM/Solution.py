// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
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