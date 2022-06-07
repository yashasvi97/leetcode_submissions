// https://leetcode.com/problems/battleships-in-a-board

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                ans += 1
        return ans