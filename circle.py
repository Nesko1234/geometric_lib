import math


def area(r):
    '''Функция принимает радиус круга(r) и возвращает площадь круга путем умножения числа пи на квадрат радиуса(math.pi * r * r)''' 
    for i in str(r):
        if i not in "0123456789":
            return 0
    if r < 0:
        return 0
    return math.pi * r * r


def perimeter(r):
    '''Функция принимает радиус круга(r) и возвращает периметр круга путем умножения числа пи на удвоенный радиус(2 * math.pi * r)'''
    for i in str(r):
        if i not in "0123456789":
            return 0
    if r < 0:
        return 0
    return 2 * math.pi * r

