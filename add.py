"""
Problem 4: Chainable Addition (add class)

Условие:
1. Реализовать класс add, поддерживающий цепочку вызовов вида add(1)(2)(3)(4) -> 10.
2. Объект должен корректно сравниваться с обычными числами: add(5) == 5 -> True.
3. Промежуточные результаты можно сохранять в переменные и переиспользовать.
"""

class add(int):
    def __call__(self, value: int) -> "add":
        # Возвращаем НОВЫЙ экземпляр add с суммой (self + value), чтобы не изменять исходный объект (immutability)
        return add(self + value)


if __name__ == "__main__":
    print(add(1)(2)(3)(4))
    print(add(5) == 5)

    a = add(1)(2)
    print(a)
    print(a(3))
    print(a)
