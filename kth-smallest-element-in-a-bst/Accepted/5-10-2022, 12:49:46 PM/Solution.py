// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(src):
            if src is not None:
                
                dfs(src.left)
                
                self.discovered += 1
                if self.discovered == k:
                    self.ans = src.val
                
                if self.ans:
                    return
                else:
                    dfs(src.right)
                
        self.discovered = 0
        self.ans = None
        
        dfs(root)
        
        return self.ans