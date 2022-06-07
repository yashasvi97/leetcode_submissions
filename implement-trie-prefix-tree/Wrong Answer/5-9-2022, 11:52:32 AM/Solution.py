// https://leetcode.com/problems/implement-trie-prefix-tree

class Node:
    def __init__(self, val=None, terminal=False):
        self.terminal = terminal
        self.val      = val
        self.children = [None] * 26
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
        if not node.terminal:
            return True
        return False
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)