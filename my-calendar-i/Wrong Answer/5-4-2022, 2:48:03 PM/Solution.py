// https://leetcode.com/problems/my-calendar-i

class Node:
    def __init__(self, start: int, end: int, left = None, right = None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def overlap(self, s1, e1):
        if s1 <= self.start:
            if self.start < e1:
                return True
        else:
            if self.end > s1:
                return True
        return False
    
    def before(self, node):
        return node.end < self.start
    
    
    def insert(self, node):
        if not self.overlap(node.start, node.end):
            if self.before(node):
                if self.left is None:
                    self.left = node
                    return True
                else:
                    return self.left.insert(node)
            else:
                if self.right is None:
                    self.right = node
                    return True
                else:
                    return self.right.insert(node)
        return False
            

class MyCalendar:    
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        newNode = Node(start, end)
        return self.root.insert(newNode)
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)