"""
Problem 3: Circle Class

Условие:
1. Реализовать свойства radius (чтение и запись через @property и @radius.setter)
   и diameter (только для чтения через @property).
2. Реализовать методы area() и circumference() для расчёта площади и длины окружности.
3. Реализовать магические методы __str__, __repr__ и __eq__ (сравнение кругов по радиусу).
"""
import math


class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius

    @property
    def radius(self) -> int | float:
        return self._radius

    @radius.setter
    def radius(self, value: int | float) -> None:
        if value < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self._radius = value

    @property
    def diameter(self) -> int | float:
        return self._radius * 2

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    def circumference(self) -> float:
        return 2 * math.pi * self._radius

    # Строковое представление для пользователя (вызывается при print(c1))
    def __str__(self) -> str:
        return f"Circle with radius: {self._radius}"

    # Техническое представление для отладки (вызывается при repr(c1))
    def __repr__(self) -> str:
        return f"Circle({self._radius})"

    # вызывается при c1 == c2
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius


if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(5)

    print(c1)
    print(c2)
    print(c1.area())
    print(c2.circumference())
    print(c1.diameter)

    print(c1 == c2)
    print(c1 == c3)

    c1.radius = 8
    print(c1)
    print(c1.area())
