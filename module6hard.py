class Figure:
    sides_count = 0

    def __init__(self, __sides: list, __color: list, filled: bool):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if isinstance(r and g and b, int) and (r and g and b <= 255) and (r and g and b > 0):
            return True

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if isinstance(args, int) and args == self.sides_count and args > 0:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return len(self.__sides)

    def set_sides(self, *new_sides):
        if len(*new_sides) == len(self.sides_count):
            self.sides_count = self.new_sides


class Circle(Figure):
    sides_count = 0
    pi = 3.14
    def __init__(self, __radius):
        super().__init__(__radius)
        __radius = self.sides_count // (2 * self.pi)

    def get_square(self):
        D = self.__radius ** 2
        S = self.pi * D
        return S

class Triangle(Figure):
    sides_count = 3
    def __init__(self):
        super().__init__()

    def get_square(self):
        p = 0.5 * (a + b + c)
        s_triangle = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s_triangle

