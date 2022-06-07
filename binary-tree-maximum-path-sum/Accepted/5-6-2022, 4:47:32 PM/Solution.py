// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def util(src):
            if src is not None:
                sum_l = util(src.left)
                sum_r = util(src.right)
                
                max_single = max(max(sum_l, sum_r) + src.val, src.val)
                
                max_top = max(max_single, sum_l+sum_r+src.val)
                
                util.res = max(max_top, util.res)
                
                return max_single
            else:
                return 0
        
        import sys
        util.res = -1*sys.maxsize
        util(root)
        return util.res