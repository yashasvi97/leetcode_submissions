// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def inorder(self, src, l=[]):
        if src is not None:
            il = self.inorder(src.left)
            il.append(src.val)
            il.extend(self.inorder(src.right))
            return il
        else:
            return []
    
    def preorder(self, src, l=[]):
        if src is not None:
            il = [src.val]
            il.extend(self.preorder(src.left))
            il.extend(self.preorder(src.right))
            return il
        else:
            return []
    
    def constructTree(self, preorder_, inorder_):
        if len(inorder_) > 0 and len(preorder_) > 0:
            root = TreeNode(val=preorder_[0])

            i = 0
            while inorder_[i] != root.val:
                i += 1
            # anything left of i (inorder) is left subtree
            root.left = self.constructTree(preorder_[1:i+1], inorder_[:i])
            root.right = self.constructTree(preorder_[i+1:], inorder_[i+1:])

            return root
        else:
            return None
            
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ino = self.inorder(root)
        # print("ino", ino)
        pre = self.preorder(root)
        # print("pre", pre)
        s = ""
        for x in ino:
            s += str(x)
        for x in pre:
            s += str(x)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        n = len(data)
        m = n//2
        ino = []
        for i in range(m):
            ino.append(int(data[i]))
        pre = []
        for i in range(m, n):
            pre.append(int(data[i]))
        
        root = self.constructTree(pre, ino)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))