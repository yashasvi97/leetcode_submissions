// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def constructBST(pre, start, end):
            if start > end:
                return None
            node = TreeNode(val=pre[start])
            i = start
            while i <= end:
                if pre[i] > node.val:
                    break
                i += 1
            node.left = constructBST(pre, start+1, i-1)
            
            node.right = constructBST(pre, i, end)
            
            return node
            
        
        root = constructBST(preorder, 0, len(preorder)-1)
        
        return root