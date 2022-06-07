// https://leetcode.com/problems/number-of-laser-beams-in-a-bank

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        dev_row = [0 for i in range(n)]
        
        for i, s in enumerate(bank):
            for j in range(len(s)):
                if s[j] == '1':
                    dev_row[i] += 1
        
        # print(dev_row)
        
        i = 0
        
        while i < n and dev_row[i] == 0:
            i += 1
        
        j = i+1
        laser = 0
        
        while i < n-1 and j <= n-1:
            if dev_row[j] == 0:
                j += 1
            else:
                laser += dev_row[i] * dev_row[j]
                i = i+1
                j = i+1
        return laser