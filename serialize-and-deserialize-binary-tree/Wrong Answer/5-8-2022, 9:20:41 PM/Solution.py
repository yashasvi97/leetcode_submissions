// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def inorder(self, src, inol):
        if src is not None:
            left = self.inorder(src.left, [])
            if len(left) != 0:
                inol.extend(left)
            inol.append(src.val)
            right = self.inorder(src.right, [])
            if len(right) != 0:
                inol.extend(right)
        return inol
    
    def preorder(self, src, prel):
        if src is not None:
            prel.append(src.val)
            left = self.preorder(src.left, [])
            if len(left) != 0:
                prel.extend(left)
            right = self.preorder(src.right, [])
            if len(right) != 0:
                prel.extend(right)
        return prel
    
    def constructTree(self, preorder, inorder):
#         def array_to_tree(left, right):
#             nonlocal preorder_index
#             # if there are no elements to construct the tree
#             if left > right: return None

#             # select the preorder_index element as the root and increment it
#             root_value = preorder[preorder_index]
#             root = TreeNode(root_value)


#             preorder_index += 1

#             # build left and right subtree
#             # excluding inorder_index_map[root_value] element because it's the root
#             root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
#             root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

#             return root

#         preorder_index = 0

#         # build a hashmap to store value -> its index relations
#         inorder_index_map = {}
#         for index, value in enumerate(inorder):
#             inorder_index_map[value] = index

#         return array_to_tree(0, len(preorder) - 1)
#         if len(inorder) > 0 and len(preorder) > 0:
#             root = TreeNode(val=preorder[0])

#             i = 0
#             while inorder[i] != root.val:
#                 i += 1
#             # anything left of i (inorder) is left subtree
#             root.left = self.constructTree(preorder[1:i+1], inorder[:i])
#             root.right = self.constructTree(preorder[i+1:], inorder[i+1:])

#             return root
#         else:
#             return None
        def return_tree(part_inorder):
            if not part_inorder:
                return None
            partition_root = preorder.pop(0)
            partition_root_index = part_inorder.index(partition_root)
            left_partition = return_tree(part_inorder[:partition_root_index])
            right_partition = return_tree(part_inorder[partition_root_index+1:])
            return TreeNode(partition_root, left_partition, right_partition)
        
        return return_tree(inorder)
            
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        else:
            ino = self.inorder(root, [])
            print(ino)
            pre = self.preorder(root, [])
            print(pre)
            
            s1 = '.'.join([str(x) for x in ino])
            s2 = '.'.join([str(x) for x in pre])
            
            return s1+'='+s2

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        else:
            [s1, s2] = data.split('=')
            ino = []
            a1 = s1.split('.')
            for x in a1:
                ino.append(int(x))

            pre = []
            a2 = s2.split('.')
            for x in a2:
                pre.append(int(x))
            root = self.constructTree(pre, ino)
            return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))