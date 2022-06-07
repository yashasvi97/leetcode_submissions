// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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