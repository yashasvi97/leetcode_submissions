// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare(nodeA, nodeB):
            if nodeA is None or nodeB is None:
                if (nodeA is None and nodeB is not None) or (nodeA is not None and nodeB is None):
                    return False
                return True
            if nodeA.val != nodeB.val:
                return False
            if compare(nodeA.left, nodeB.left) and compare(nodeA.right, nodeB.right):
                return True
            return False
        return compare(p, q)