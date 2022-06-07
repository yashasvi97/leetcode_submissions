// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(src, discovered):
            if src is None:
                return
            left = dfs(src.left, discovered)
            if left is not None:
                return left
            
            discovered += 1
            if discovered == k:
                return src.val
            
            return dfs(src.right, discovered)
        
        return dfs(root, 0)