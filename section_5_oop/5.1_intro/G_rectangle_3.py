class Rectangle:

    def __init__(self, corner1, corner2) -> None:
        self.down_left = [
            min(corner1[0], corner2[0]),
            min(corner1[1], corner2[1])
        ]
        self.up_right = [
            max(corner1[0], corner2[0]),
            max(corner1[1], corner2[1])
        ]
        self.rotations = 0

    def perimeter(self):
        return round(
            (self.up_right[0] - self.down_left[0]) * 2 +
            (self.up_right[1] - self.down_left[1]) * 2,
            2,
        )

    def area(self):
        return round(
            (self.up_right[0] - self.down_left[0]) *
            (self.up_right[1] - self.down_left[1]),
            2,
        )

    def get_pos(self):
        return round(self.down_left[0], 2), round(self.up_right[1], 2)

    def get_size(self):
        return round(self.up_right[0] - self.down_left[0],
                     2), round(self.up_right[1] - self.down_left[1], 2)

    def move(self, dx, dy):
        self.down_left[0] += dx
        self.down_left[1] += dy
        self.up_right[0] += dx
        self.up_right[1] += dy

    def resize(self, width, height):
        self.up_right[0] = self.down_left[0] + width
        self.down_left[1] = self.up_right[1] - height

    def turn(self):
        sizes = list(self.get_size())
        a = round((max(sizes) - min(sizes)) / 2, 2)
        if self.rotations == 0:
            self.down_left[0] = self.down_left[0] + a
            self.down_left[1] = self.down_left[1] - a
            self.up_right[0] = self.up_right[0] - a
            self.up_right[1] = self.up_right[1] + a
        elif self.rotations == 1:
            self.down_left[0] = self.down_left[0] - a
            self.down_left[1] = self.down_left[1] + a
            self.up_right[0] = self.up_right[0] + a
            self.up_right[1] = self.up_right[1] - a
        self.rotations = (self.rotations + 1) % 2

    def scale(self, factor):
        sizes = list(self.get_size())
        x_add = round((sizes[0] * factor - sizes[0]) / 2, 2)
        y_add = round((sizes[1] * factor - sizes[1]) / 2, 2)
        self.down_left[0] = self.down_left[0] - x_add
        self.down_left[1] = self.down_left[1] - y_add
        self.up_right[0] = self.up_right[0] + x_add
        self.up_right[1] = self.up_right[1] + y_add


rect = Rectangle((0, 0), (5, 2))
print(rect.get_pos(), rect.get_size(), sep="\n")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep="\n")

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep="\n")
rect.turn()
print("Rect.turn() ", rect.get_pos(), rect.get_size())
rect.turn()
print("Rect.turn() ", rect.get_pos(), rect.get_size())
rect.turn()
print("Rect.turn() ", rect.get_pos(), rect.get_size())
rect.turn()
print("Rect.turn() ", rect.get_pos(), rect.get_size())
rect.turn()
print("Rect.turn() ", rect.get_pos(), rect.get_size())
