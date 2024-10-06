class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        import math

        return round(math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2),
                     2)
