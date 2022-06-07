// https://leetcode.com/problems/design-add-and-search-words-data-structure

class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False
        
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            
        node.terminal = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    # print(type(curr))
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.terminal
                    
            
            
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)