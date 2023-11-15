# Дано целое число N(>0), являющейся некоторой степенью числа 2: N=2**K. Найти целое число K - показатель этой степени.




# Exception Handling
while True:
    try:
        a = float(input("input number"))
        if a <= 0:
            print("exponent must be more than zero")
            continue
    except ValueError:
        print("something went wrong")
        continue
    break

i = 0
while a > 1:
    a = a / 2
    i += 1

print(f"Показатель степени числа 2: {i}")
