"""
    16.3 Intersection: Solution
"""

def intersection(start1, end1, start2, end2):
    if start1.x > end1.x:
        start1, end1 = end1, start1
    if start2.x > end2.x:
        start2, end2 = end2, start2
    if start1.x > start2.x:
        end1, end2 = end2, end1

    line1 = Line(start1, end1)
    line2 = Line(start2, end2)

    if (line1.slope == line2.slope):
        if line1.yintercept == line2.yintercept and isBetween(start1, start2, end2):
            return start2
        return None

    x = (line2.yintercept - line1.yintercept) / (line1.slope - line2.slope)
    y = x * line1.slope + line1.yintercept
    intersection = Point(x, y)

    if isBetween(start1, intersection, end1) and isBetween(start2, intersection, end2):
        return intersection

    return None

def isBetween_(start, middle, end):
    if start > end:
        return end <= middle and middle <= start
    else:
        return start <= middle and middle <= end

def isBetween(start, middle, end):
    return isBetween_(start.x, middle.x, end.x) and isBetween(start.y, middle.y, end.y)

class Line:
    def __init__(self, start, end):
        deltaY = end.y - start.y
        deltaX = end.x - start.x
        self.slope = deltaY / deltaX
        self.yintercept = end.y - self.slope * end.x

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setLocation(self, x, y): # not useful here as we use native variable swap in Python
        self.x = x
        self.y = y

if __name__ == "__main__":
    # TODO: Test the program and check the code
    pass