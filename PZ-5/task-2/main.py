# Дан прямоугольник, длины сторон которого равны натуральным числам A и B. Составить функцию, которая будет находить на
# сколько квадратов можно разрезать данный прямоугольник, если от него каждый раз отнимать отрезать квадрат наибольшей
# площади

while True:
    try:
        a = int(input("введите длину прямоугольника"))
        b = int(input("введите ширину прямоугольника"))
        break
    except ValueError:
        print("что-то пошло не так")
        continue


def number_of_square(a,b):
    if a>b:
        a = a//b
        return a

    elif b>a:
        b = b//a
        return b

print(f"количество квадратов: {number_of_square(a,b)}")



