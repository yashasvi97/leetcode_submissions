// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(source):
            if source is None:
                return -1
            l = dfs(source.left)
            r = dfs(source.right)
            
            d = l + r + 2
            res[0] = max(res[0], d)
            
            return 1 + max(l, r)
        dfs(root)
        return res[0]