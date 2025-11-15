def area(a, h):
    '''Функция принимает длину стороны треугольника и высоту, опирающуюся на эту сторону,(a, h) и возвращает площадь треугольника путем перемножения длины стороны этого треугольника, длины высоты этого треугольника и одной второй(a * h / 2)'''
    for i in str(a):
        if i not in "0123456789":
            return 0
    if a < 0:
        return 0
    for i in str(h):
        if i not in "0123456789":
            return 0
    if h < 0:
        return 0
    return a * h / 2
def perimeter(a, b, c):
    '''Функция принимает длины всех сторон треугольника(a, b, c) и возвращает периметр этого трегольника путем сложения длин всех сторон(a + b + c)'''
    for i in str(a):
        if i not in "0123456789":
            return 0
    if a < 0:
        return 0
    for i in str(b):
        if i not in "0123456789":
            return 0
    if b < 0:
        return 0
    for i in str(c):
        if i not in "0123456789":
            return 0
    if c < 0:
        return 0
    return a + b + c