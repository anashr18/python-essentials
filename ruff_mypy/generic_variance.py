from typing import Sequence


class Shape:
    pass


class Circle(Shape):
    # The rotate method is only defined on Circle, not on Shape
    def rotate(self): ...


# def add_one(things: list[Shape]) -> None:


def add_one(things: Sequence[Shape]) -> None:
    things.append(Shape())


my_circles: list[Circle] = []
add_one(my_circles)  # This may appear safe, but...
my_circles[-1].rotate()
