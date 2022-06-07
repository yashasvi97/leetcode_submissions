// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, source):
        if source is None:
            return 0
        else:
            return 1 + max(self.height(source.left), self.height(source.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            dl = self.diameterOfBinaryTree(root.left)
            dr = self.diameterOfBinaryTree(root.right)
            
            hl = self.height(root.left)
            hr = self.height(root.right)
            
            return max(hl+hr, max(dl, dr))