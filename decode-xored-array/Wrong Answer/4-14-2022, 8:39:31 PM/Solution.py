// https://leetcode.com/problems/decode-xored-array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for x in encoded:
            k = arr[-1]
            arr.append(abs(x-k))
        return arr