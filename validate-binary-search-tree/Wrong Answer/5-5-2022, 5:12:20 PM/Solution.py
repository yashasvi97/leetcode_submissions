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
        discovered = []
        def preorder(source):
            if source is not None:
                preorder(source.left)
                discovered.append(source.val)
                preorder(source.right)
        preorder(root)
        # print(discovered)
        sdisc = sorted(discovered)
        return all([x == y for (x, y) in zip(discovered, sdisc)])