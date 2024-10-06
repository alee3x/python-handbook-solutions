class Rectangle:

    def __init__(self, A, B):
        self.corner_1 = A
        self.corner_2 = B

    def perimeter(self):
        abscissa = abs(self.corner_1[0] - self.corner_2[0])
        ordinate = abs(self.corner_1[1] - self.corner_2[1])
        return round(abscissa * 2 + ordinate * 2, 2)

    def area(self):
        abscissa = abs(self.corner_1[0] - self.corner_2[0])
        ordinate = abs(self.corner_1[1] - self.corner_2[1])
        return round(abscissa * ordinate, 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
