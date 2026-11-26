"""
Problem 6: Matrix Class (My_matrix)

Условие:
1. Реализовать класс My_matrix с атрибутами/свойствами rows и columns.
2. Поддержать итерацию по строкам (__iter__), индексацию matrix[i][j] (__getitem__)
   и красивый построчный вывод (__str__).
3. Реализовать методы is_square() (проверка на квадратность) и trace() (след матрицы).
4. Реализовать операции сложения (+), вычитания (-) и умножения (*) на число и на матрицу.
"""


class My_matrix:
    def __init__(self, data: list[list[int | float]]):
        if not data or not data[0]:
            raise ValueError("Матрица не может быть пустой")

        row_length = len(data)
        for row in data:
            if len(row) != row_length:
                raise ValueError("Все строки матрицы должны быть одинаковой длины")

        self.data = [row[:] for row in data]

    @property
    def rows(self) -> int:
        return len(self.data)

    @property
    def columns(self) -> int:
        return len(self.data[0])

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index: int) -> list[int | float]:
        return self.data[index]

    def __str__(self) -> str:
        return "\n".join(str(row) for row in self.data)

    def __repr__(self) -> str:
        return f"My_matrix({self.data})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, My_matrix):
            return NotImplemented
        return self.data == other.data

    def is_square(self) -> bool:
        return self.rows == self.columns

    def trace(self) -> int | float:
        if not self.is_square():
            raise ValueError("След можно вычислить только для квадратной матрицы")
        return sum(self.data[i][i] for i in range(self.rows))

    def __add__(self, other: "My_matrix") -> "My_matrix":
        if not isinstance(other, My_matrix):
            return NotImplemented
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Для сложения матрицы должны быть одинакового размера")

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.columns)]
            for i in range(self.rows)
        ]
        return My_matrix(result)

    def __sub__(self, other: "My_matrix") -> "My_matrix":
        if not isinstance(other, My_matrix):
            return NotImplemented
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Для вычитания матрицы должны быть одинакового размера")

        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.columns)]
            for i in range(self.rows)
        ]
        return My_matrix(result)

    def __mul__(self, other: "int | float | My_matrix") -> "My_matrix":
        if isinstance(other, (int, float)):
            result = [
                [self.data[i][j] * other for j in range(self.columns)]
                for i in range(self.rows)
            ]
            return My_matrix(result)

        if isinstance(other, My_matrix):
            if self.columns != other.rows:
                raise ValueError(
                    "Число столбцов первой матрицы должно равняться числу строк второй"
                )
            result = [
                [
                    sum(self.data[i][k] * other.data[k][j] for k in range(self.columns))
                    for j in range(other.columns)
                ]
                for i in range(self.rows)
            ]
            return My_matrix(result)

        return NotImplemented

    def __rmul__(self, other: int | float) -> "My_matrix":
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented


if __name__ == "__main__":
    m1 = My_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = My_matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print("Матрица m1:")
    print(m1)
    print("Строк:", m1.rows, "Столбцов:", m1.columns)
    print("Элемент [2][0]:", m1[2][0])
    print("Квадратная:", m1.is_square())
    print("След матрицы m1:", m1.trace())

    print("\nСумма m1 + m2:")
    print(m1 + m2)

    print("\nРазность m1 - m2:")
    print(m1 - m2)

    print("\nУмножение m1 * 2:")
    print(m1 * 2)

    print("\nМатричное умножение m1 * m2:")
    print(m1 * m2)
