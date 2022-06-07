// https://leetcode.com/problems/design-add-and-search-words-data-structure

class Node:
    def __init__(self, val=None, terminal=False):
        self.children = [None] * 26
        self.val      = val
        self.terminal = terminal
        
class WordDictionary:

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
    
    def addWord(self, word: str) -> None:
        self.insert(word)

    def helper(self, node: Node,  word: str) -> bool:
        if self.i > len(word): return False
        if self.i == len(word):
            
            if node.terminal:
                return True
            return False
        x = word[self.i]
        if x == '.':
            f = 0
            for i in range(len(node.children)):
                if node.children[i] is not None:
                    self.i += 1
                    y = self.helper(node.children[i], word)
                    if y is False:
                        self.i -= 1
                    else:
                        f = 1
                        break
            if f:
                return True
        else:
            ind = ord(x) - ord('a')
            if node.children[ind] is None:
                return False
            
            self.i += 1
            
            return self.helper(node.children[ind], word)
        
        return False
    
    def search(self, word: str) -> bool:
        self.i = 0
        return self.helper(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)