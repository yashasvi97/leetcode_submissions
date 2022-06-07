// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            dl = self.diameterOfBinaryTree(root.left)
            dr = self.diameterOfBinaryTree(root.right)
            stack = [(root, 1)]
            max_depth = 1
            while len(stack) != 0:
                (v, depth) = stack.pop()
                max_depth = max([depth, max_depth])
                if v.left is not None:
                    stack.append((v.left, depth+1))
                if v.right is not None:
                    stack.append((v.right, depth+1))
            return max([dl, dr, max_depth])
        else:
            return 0