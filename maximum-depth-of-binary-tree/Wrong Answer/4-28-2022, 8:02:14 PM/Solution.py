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
            visited = [False] * 10001
            distance = [-1] * 10001
            
            maxDepth = 1
            
            stack.append(root)
            distance[root.val] = 1
            prev_dist = distance[root.val]
            while len(stack) != 0:
                v = stack.pop()
                if not visited[v.val]:
                    visited[v.val] = True
                    distance[v.val] = prev_dist + 1
                    c = 0
                    for neighbor in ["left", "right"]:
                        u = getattr(v, neighbor)
                        if u is not None:
                            stack.append(u)
                        else:
                            c += 1
                    if c == 2:
                        maxDepth = max([maxDepth, distance[v.val]])
            return maxDepth