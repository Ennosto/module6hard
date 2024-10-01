class Figure:
    sides_count = 0

    def __init__(self, sides: int, color: int, filled: bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and 0 <= r <= 255 and isinstance(g, int) and 0 <= g <= 255 and isinstance(b, int) and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if isinstance(sides, int) and sides > 0 and len(sides) == self.sides_count:
            return True
        else:
            return False
