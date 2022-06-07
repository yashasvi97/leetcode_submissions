// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n
        while True:
            m = (l+h)//2
            if isBadVersion(m) and not isBadVersion(m-1):
                break
            else:
                if isBadVersion(m):
                    h = m
                else:
                    l = m+1
        return m