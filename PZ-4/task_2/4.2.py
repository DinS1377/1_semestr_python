# Дано целое число N(>0), являющейся некоторой степенью числа 2: N=2**K. Найти целое число K - показатель этой степени.


# обработка исключений
while True:
    try:
        a = float(input("введите число"))
        if a <= 0:
            print("число должно быть больше нуля")
            continue
    except ValueError:
        print("что-то пошло не так")
        continue
    break

i = 0
while a > 1:
    a = a / 2
    i += 1

print(f"Показатель степени числа 2: {i}")