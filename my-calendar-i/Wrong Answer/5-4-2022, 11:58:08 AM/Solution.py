// https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.timeline = []

    def book(self, start: int, end: int) -> bool:
        for (s, e) in self.timeline:
            if start >= s and start < e:
                return False
            if end >= s and end < e:
                return False
        self.timeline.append((start, end))
        self.timeline = sorted(self.timeline, key=lambda x: x[0])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)