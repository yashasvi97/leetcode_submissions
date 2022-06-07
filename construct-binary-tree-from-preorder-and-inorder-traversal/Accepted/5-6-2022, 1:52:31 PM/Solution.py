// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        
#         h = {}
#         for idx, val in enumerate(inorder):
#             h[val] = idx
        
#         def helper(pre):
#             if len(pre) > 0:
#                 root = TreeNode(val=pre[0])

#                 i = h[root.val]

#                 # anything left of i (inorder) is left subtree
#                 root.left  = helper(pre[1:i+1])
#                 root.right = helper(pre[i+1:])

#                 return root
#             else:
#                 return None
        
#         return helper(preorder)
        if len(inorder) > 0 and len(preorder) > 0:
            root = TreeNode(val=preorder[0])

            i = 0
            while inorder[i] != root.val:
                i += 1
            # anything left of i (inorder) is left subtree
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

            return root
        else:
            return None