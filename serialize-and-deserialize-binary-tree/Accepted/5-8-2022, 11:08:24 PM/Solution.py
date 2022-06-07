// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def preorder(self, src, s):
        if src is not None:
            s += (str(src.val) + " ")
            s += self.preorder(src.left, "")
            s += self.preorder(src.right, "")
        else:
            s += "# "
        return s
    
    def constructTree(self, order):
        if self.index > len(order): return None
        if order[self.index] == '#': return None
        root = TreeNode(val=int(order[self.index]))
        self.index += 1
        root.left = self.constructTree(order)
        self.index += 1
        root.right = self.constructTree(order)
        return root
            
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pre = self.preorder(root, "")
        # print(pre)
        return pre

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.index = 0
        a2 = data.split(' ')[:-1]
        # print(a2)
        return self.constructTree(a2)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))