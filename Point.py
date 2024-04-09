class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        # Растояние от точки до точки
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return round(distance, 2)

    def distance_to_zero(self):
        distance = ((self.x) ** 2 + (self.y) ** 2) ** 0.5
        return round(distance, 2)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

point_a = Point(1, 2)
point_b = Point(3, 4)

print(point_a.distance_to(point_b))
print(point_a.distance_to_zero())