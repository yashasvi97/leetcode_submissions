// https://leetcode.com/problems/maximum-score-words-formed-by-letters

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = [0]*26
        for l in letters:
            count[ord(l)-ord('a')] += 1
        
        
        def helper(_words, start, _count, _score):
            if start == len(_words):
                return 0
            
            
            counts = _count
            currScore = 0
            wordScore = 1
            for i in range(len(_words[start])):
                idx = ord(_words[start][i]) - ord('a')
                if counts[idx] == 0:
                    wordScore = -1
                    break
                wordScore += _score[idx]
                counts[idx] -= 1
            if wordScore > 0:
                currScore = helper(_words, start+1, counts, _score) + wordScore
                
            currScore = max(currScore, helper(_words, start+1, _count, _score))
            return currScore
            
        return helper(words, 0, count, score)