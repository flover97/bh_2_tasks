import math


"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Функция triangle получает длины 2х катетов прямоугольного тругольника.
Нужно отредактировать функцию таким образом,
чтобы она возвращала периметр, площадь и гипотенузу

ПРИМЕРЫ
--------------------------------------------------------------------------------
triangle(3, 4) -> (5, 12, 6)
"""


def triangle(side1: int, side2: int) -> tuple:
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    perimeter = side1 + side2 + math.sqrt(side1 ** 2 + side2 ** 2)
    square = side1 * side2 / 2
    return hypotenuse, perimeter, square


if __name__ == '__main__':
    side1_val = int(input('Введите длину первого катета: '))
    side2_val = int(input('Введите длину второго катета: '))
    print(f'(Гипотенуза, Периметр, Площадь): {triangle(side1_val, side2_val)}')
