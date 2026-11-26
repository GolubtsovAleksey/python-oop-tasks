"""
Problem 5: Number Wrapper Class

Условие:
1. Реализовать класс Number, хранящий целое число.
2. Поддержать получение цифры числа по индексу через квадратные скобки: num[index] -> int.
3. Поддержать операции умножения (*) и вычитания (-), возвращающие новый объект Number,
   чтобы работали цепочки вида (num - 320) * 5 и (num - 320)[0].
"""


class Number:
    def __init__(self, value: int):
        self.value = value

    def __getitem__(self, index: int) -> int:
        digits = str(abs(self.value))
        return int(digits[index])

    def __sub__(self, other: "int | Number") -> "Number":
        other_value = other.value if isinstance(other, Number) else other
        return Number(self.value - other_value)

    def __mul__(self, other: "int | Number") -> "Number":
        other_value = other.value if isinstance(other, Number) else other
        return Number(self.value * other_value)

    def __rmul__(self, other: int) -> "Number":
        return self.__mul__(other)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Number({self.value})"


if __name__ == "__main__":
    num = Number(421)
    print(num[1])
    print(num * 2)
    print((num - 320) * 5)
    print((num - 320)[0])
