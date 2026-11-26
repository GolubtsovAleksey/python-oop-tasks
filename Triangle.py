"""
Problem 1: Triangle Class

Условие:
1. Создать класс Triangle. Конструктор __init__() принимает self, angle1, angle2 и angle3
   и сохраняет их как атрибуты экземпляра.
2. Создать атрибут класса number_of_sides = 3.
3. Создать метод check_angles(), который возвращает True, если сумма трёх углов равна 180,
   и False в противном случае.
4. Создать экземпляр my_triangle со значениями углов (90, 30, 60),
   вывести my_triangle.number_of_sides и результат my_triangle.check_angles().
"""

class Triangle:
    # Атрибут класса общий для всех треугольников
    number_of_sides = 3

    def __init__(self, angle1: int | float, angle2: int | float, angle3: int | float):
        # Атрибуты экземпляра (поля конкретного объекта)
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self) -> bool:
        return self.angle1 + self.angle2 + self.angle3 == 180


if __name__ == "__main__":
    my_triangle = Triangle(90, 30, 60)
    print(my_triangle.number_of_sides)
    print(my_triangle.check_angles())
