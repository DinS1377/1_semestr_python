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



