// https://leetcode.com/problems/my-calendar-i

class MyCalendar:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    def overlap(self, s1, e1, s2, e2):
        if s1 <= s2:
            if s2 < e1:
                return True
        else:
            if e2 > s1:
                return True
        return False
    
    def __init__(self):
        self.timeline = []

    def book(self, start: int, end: int) -> bool:
        for (s, e) in self.timeline:
            if self.overlap(s, e, start, end):
                return False
        self.timeline.append((start, end))
        # self.timeline = sorted(self.timeline, key=lambda x: x[0])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)