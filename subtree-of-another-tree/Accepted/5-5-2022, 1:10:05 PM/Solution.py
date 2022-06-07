// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(nodeA, nodeB):
            if nodeA is None or nodeB is None:
                if (nodeA is None and nodeB is not None) or (nodeA is not None and nodeB is None):
                    return False
                return True
            if nodeA.val == nodeB.val and compare(nodeA.left, nodeB.left) and compare(nodeA.right, nodeB.right):
                return True
            else:
                return False
    
        def DFS(source, search):
            stack = [(source, 1)]
            f = 0
            while len(stack) != 0:
                (n, d) = stack.pop()
                if n.val == search.val:
                    if compare(n, search):
                        f = 1
                        break
                if n.right is not None:
                    stack.append((n.right, d+1))
                if n.left is not None:
                    stack.append((n.left, d+1))
            if f:
                return True
            else:
                return False
        return DFS(root, subRoot)