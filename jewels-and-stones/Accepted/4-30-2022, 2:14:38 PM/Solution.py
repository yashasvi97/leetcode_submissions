// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = 0
        for i in range(len(stones)):
            c = stones[i]
            if c in jewels:
                x += 1
        return x