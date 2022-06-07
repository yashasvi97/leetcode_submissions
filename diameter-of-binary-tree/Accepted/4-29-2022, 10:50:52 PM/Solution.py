// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_height(self, source):
        if source is None:
            return 0
        else:
            return 1 + max([self.max_height(source.left), self.max_height(source.right)])
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lh = self.max_height(root.left)
        rh = self.max_height(root.right)
        
        dl = self.diameterOfBinaryTree(root.left)
        dr = self.diameterOfBinaryTree(root.right)
        return max([lh+rh, max([dl, dr])])