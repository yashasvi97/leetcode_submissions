// https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hash_tab = [0] * 10001
        for n in nums:
            hash_tab[n] += n
        for i in range(2, 10001):
            hash_tab[i] = max([hash_tab[i-1], hash_tab[i-2]+hash_tab[i]])
        return hash_tab[10000]