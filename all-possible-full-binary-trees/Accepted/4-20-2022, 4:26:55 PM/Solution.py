// https://leetcode.com/problems/all-possible-full-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        if n %2 == 0:
            return res
        if n == 1:
            node = TreeNode(val=0)
            res.append(node)
        for i in range(1, n-1, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-1-i)
            for l in left:
                for r in right:
                    root = TreeNode(val=0)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
            