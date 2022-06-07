// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        dup = 0
        tot_dup = 0
        i = 0
        j = 1
        while i < n-1:
            val_i = nums[i]
            while j <= (n-1) and nums[j] == val_i:
                dup = 1
                j += 1
            if dup == 1:
                if j == n:
                    break
                n_dup = j - i - 1
                tot_dup += n_dup
                
                # sub_arr = nums[j:n]
                # nums[i+1:i+1+n_dup] = sub_arr
                
                for k in range(j, n):
                    nums[k-n_dup] = nums[k]
                
                n -= n_dup
                nums[n] = -101
                '''
                while n_dup > 0:
                    for k in range(j, n):
                        nums[k-1] = nums[k]
                    j -= 1
                    nums[n-1] = -101
                    n -= 1
                    n_dup -= 1'''
                dup = 0
            i = i + 1
            j = i + 1
        if dup == 1:
            n_dup = j - i - 1
            tot_dup += n_dup
            if i == 0 and tot_dup == n:
                return 1
            
            # sub_arr = nums[j:n]
            # nums[i+1:i+1+n_dup] = sub_arr
            
            for k in range(j, n):
                nums[k-n_dup] = nums[k]
            
            n -= n_dup
            nums[n] = -101
            '''
            while n_dup > 0:
                for k in range(j, n):
                    nums[k-1] = nums[k]
                j -= 1
                nums[n-1] = -101
                n -= 1
                n_dup -= 1'''
        k_val = n
        return k_val