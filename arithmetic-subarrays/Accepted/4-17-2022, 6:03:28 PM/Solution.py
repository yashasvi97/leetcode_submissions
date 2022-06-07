// https://leetcode.com/problems/arithmetic-subarrays

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for (l_, r_) in zip(l, r):
            sub = nums[l_:r_+1]
            sub.sort()
            n = len(sub)
            if n > 1:
                test = sub[1] - sub[0]
                f = 0
                for i in range(1, n-1):
                    if sub[i+1]-sub[i] != test:
                        f = 1
                        break
                if f == 1:
                    answer.append(False)
                else:
                    answer.append(True)
        return answer
                        