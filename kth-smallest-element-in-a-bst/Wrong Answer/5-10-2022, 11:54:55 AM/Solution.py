// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        discovered = []
        def inorder(source):
            if source is not None:
                inorder(source.left)
                discovered.append(source.val)
                # num += 1
                if len(discovered) == k:
                    return
                inorder(source.right)
        
        inorder(root)
        return discovered[-1]