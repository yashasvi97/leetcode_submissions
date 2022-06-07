// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            stack = []
            
            maxDepth = 1
            
            stack.append(root)
            setattr(root, "dist", 1)
            setattr(root, 'visited', False)
            while len(stack) != 0:
                v = stack.pop()
                if not getattr(v, 'visited'):
                    setattr(v, 'visited', True)
                    c = 0
                    for neighbor in ["left", "right"]:
                        u = getattr(v, neighbor)
                        if u is not None:
                            stack.append(u)
                            d = getattr(v, "dist")
                            setattr(u, "dist", d + 1)
                            setattr(u, 'visited', False)
                        else:
                            c += 1
                    if c == 2:
                        maxDepth = max([maxDepth, getattr(v, "dist")])
            return maxDepth