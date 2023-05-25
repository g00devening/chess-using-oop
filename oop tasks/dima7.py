class BoundingRectangle:
    x_coord = []
    y_coord = []
    def add_point(self, x, y):
        self.x_coord.append(x)
        self.y_coord.append(y)

    def bottom_y(self):
        return min(self.y_coord)

    def top_y(self):
        return max(self.y_coord)

    def left_x(self):
        return min(self.x_coord)

    def right_x(self):
        return max(self.x_coord)

    def width(self):
        return max(self.x_coord) - min(self.x_coord)

    def height(self):
        return max(self.y_coord) - min(self.y_coord)


rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())