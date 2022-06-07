// https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            # print(root.val)
            if root.left and root.right:
                temp = root.right
                root.right = root.left
                root.left = temp
                self.invertTree(root.left)
                self.invertTree(root.right)
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
                self.invertTree(root.right)
            elif not root.left and root.right:
                root.left = root.right
                root.right = None
                self.invertTree(root.left)
            return root