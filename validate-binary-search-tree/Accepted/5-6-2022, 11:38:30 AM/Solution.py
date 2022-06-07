// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(source, min_=None, max_=None):
            if source is None:
                return True
            if (min_ is not None and source.val <= min_) or (max_ is not None and source.val >= max_):
                return False
            if (not checkBST(source.left, min_, source.val)) or (not checkBST(source.right, source.val, max_)):
                return False
            return True
        return checkBST(root)