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
        print(word)
        print(self.i)
        if self.i > len(word): return False
        if self.i == len(word):
            print('why not here')
            if node.terminal:
                print('finally', node.val)
                return True
            return False
        x = word[self.i]
        print(self.i, x)
        if x == '.':
            print(len(node.children))
            for i in range(len(node.children)):
                if node.children[i] is not None:
                    print(chr(i+97), self.i)
                    self.i += 1
                    print(chr(i+97), self.i)
                    y = self.helper(node.children[i], word)
                    if y is False:
                        self.i -= 1
                    else:
                        return True
        else:
            ind = ord(x) - ord('a')
            if node.children[ind] is None:
                return False
            print('here', ind)
            self.i += 1
            print(self.i)
            return self.helper(node.children[ind], word)
    def search(self, word: str) -> bool:
        self.i = 0
        print(word)
        return self.helper(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)