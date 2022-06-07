// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            h = {}
            stack = [(root, 1)]
            while len(stack) != 0:
                (n, d) = stack.pop()
                if d in h:
                    h[d].append(n.val)
                else:
                    h[d] = [n.val]
                if n.right is not None:
                    stack.append((n.right, d+1))
                if n.left is not None:
                    stack.append((n.left, d+1))
            depths = sorted(list(h.keys()))
            level = []
            for d in depths:
                level.append(h[d])
            return level