// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tab_s = {}
        for i in range(len(s)):
            if s[i] in tab_s:
                tab_s[s[i]] += 1
            else:
                tab_s[s[i]] = 1
        tab_t = {}
        for i in range(len(t)):
            if t[i] in tab_t:
                tab_t[t[i]] += 1
            else:
                tab_t[t[i]] = 1
        out = True
        for k in tab_t:
            if k not in tab_s:
                out = False
                break
        return out