// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        dup = 0
        tot_dup = 0
        i = 0
        j = 1
        #set_trace()
        while i < n-1:
            val_i = nums[i]
            #j = i + 1
            while j <= (n-1) and nums[j] == val_i:
                dup = 1
                j += 1
            if dup == 1:
                if j == n:
                    break
                n_dup = j - i - 1
                tot_dup += n_dup 
                while n_dup > 0:
                    for k in range(j, n):
                        nums[k-1] = nums[k]
                    j -= 1
                    nums[n-1] = -1
                    n -= 1
                    n_dup -= 1
                dup = 0
            i = i + 1
            j = i + 1
        if dup == 1:
            n_dup = j - i - 1
            tot_dup += n_dup
            while n_dup > 0:
                for k in range(j, n):
                    nums[k-1] = nums[k]
                j -= 1
                nums[n-1] = -1
                n -= 1
                n_dup -= 1
            '''if j != (i+1):
                tot_dup += (j-i-1)'''
        k_val = 0
        while k_val < n and nums[k_val] != -1:
            k_val += 1
        #print(k_val, nums)
        return k_val