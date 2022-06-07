// https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        
        while True:
            m = (l+h)//2
            # print(m)
            if guess(m) == 0:
                break
            elif guess(m) > 0:
                l = m+1
            else:
                h = m
        return m