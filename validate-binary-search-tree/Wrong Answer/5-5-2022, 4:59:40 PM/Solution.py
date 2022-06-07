// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkleft(self, node):
        return node.left.val < node.val
    
    def checkright(self, node):
        return node.val < node.right.val
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            if root.left is not None and root.right is not None:
                if self.checkleft(root) and self.checkright(root):
                    f1 = self.isValidBST(root.left)
                    f2 = self.isValidBST(root.right)
                    return (f1 and f2)
                else:
                    return False
            if root.left is not None and root.right is None:
                if self.checkleft(root):
                    f1 = self.isValidBST(root.left)
                    return f1
                else:
                    return False
            if root.left is None and root.right is not None:
                if self.checkright(root):
                    f2 = self.isValidBST(root.right)
                    return f2
                else:
                    return False
            if root.left is None and root.right is None:
                return True