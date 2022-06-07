// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_height(self, source):
        if not source:
            return 0
        max_depth = 0
        stack = [(source, 1)]
        while len(stack) != 0:
            (v, depth) = stack.pop()
            max_depth = max(max_depth, depth)
            if v.left:
                stack.append((v.left, depth+1))
            if v.right:
                stack.append((v.right, depth+1))
        return max_depth
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.max_height(root.left)
        rh = self.max_height(root.right)
        
        dl = self.diameterOfBinaryTree(root.left)
        dr = self.diameterOfBinaryTree(root.right)
        return max(lh+rh+1, max(dl, dr))-1