// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tab = {}
        for x in nums:
            if x not in tab.keys():
                tab[x] = 1
            else:
                 tab[x] += 1
        sortedk = sorted(tab, key=lambda s: tab[s], reverse=True)
        topk = sortedk[:k]
        return topk
        