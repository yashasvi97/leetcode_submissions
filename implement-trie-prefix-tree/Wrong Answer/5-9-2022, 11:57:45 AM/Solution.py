// https://leetcode.com/problems/implement-trie-prefix-tree

class Node:
    def __init__(self, val=None, terminal=False):
        self.terminal = terminal
        self.val      = val
        self.children = [None] * 26
    # def __str__(self):
    #     print(self.val, self.terminal)
    #     for i in range(26):
    #         if self.children[i] is not None:
    #             print(self.children[i].val, end=", ")
    #     print("")
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word):
            x = word[i]
            
            ind = ord(x) - ord('a')
            
            if node.children[ind] is None:
                node.children[ind] = Node(val=x)
            node = node.children[ind]
            
            i += 1
            
        node.val = word
        node.terminal = True
        # print(self.root)

    def search(self, word: str) -> bool:
        i = 0
        node = self.root
        while i < len(word):
            x = word[i]
            ind = ord(x) - ord('a')
            
            if node.children[ind] is None:
                return False
            node = node.children[ind]
            
            i += 1
        # print(node.val, node.terminal)
        if node.val == word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        i = 0
        node = self.root
        while i < len(prefix):
            x = prefix[i]
            ind = ord(x) - ord('a')
            
            if node.children[ind] is None:
                return False
            node = node.children[ind]
            
            i += 1
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)