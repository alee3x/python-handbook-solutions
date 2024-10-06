class Rectangle:

    def __init__(self, corner1, corner2) -> None:
        self.left_down = [
            min(corner1[0], corner2[0]),
            min(corner1[1], corner2[1])
        ]
        self.up_right = [
            max(corner1[0], corner2[0]),
            max(corner1[1], corner2[1])
        ]

    def perimeter(self):
        return round(
            (self.up_right[0] - self.left_down[0]) * 2 +
            (self.up_right[1] - self.left_down[1]) * 2,
            2,
        )

    def area(self):
        return round(
            (self.up_right[0] - self.left_down[0]) *
            (self.up_right[1] - self.left_down[1]),
            2,
        )

    def get_pos(self):
        return round(self.left_down[0], 2), round(self.up_right[1], 2)

    def get_size(self):
        return round(self.up_right[0] - self.left_down[0],
                     2), round(self.up_right[1] - self.left_down[1], 2)

    def move(self, dx, dy):
        self.left_down[0] += dx
        self.left_down[1] += dy
        self.up_right[0] += dx
        self.up_right[1] += dy

    def resize(self, width, height):
        self.up_right[0] = self.left_down[0] + width
        self.left_down[1] = self.up_right[1] - height
