// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        letters = []
        for i in range(len(s)):
            letters.append(s[i])
        loc = []
        for i in range(len(s)):
            if s[i] in vowels:
                loc.append(i)
        for i in range(len(loc)//2):
            # swap these
            t_c = letters[loc[i]]
            letters[loc[i]] = letters[loc[len(loc)-i-1]]
            letters[loc[len(loc)-1-i]] = t_c
        rs = ''.join([z for z in letters])
        return rs