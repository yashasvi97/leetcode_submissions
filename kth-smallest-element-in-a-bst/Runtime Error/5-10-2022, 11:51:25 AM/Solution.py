// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        def inorder(source, num):
            if source is not None:
                left = inorder(source.left)
                if left is not None: return left
                # source.val
                num += 1
                if num == k: 
                    return source
                return inorder(source.right)
            else:
                return source
        
        
        
        return inorder(root, num).val