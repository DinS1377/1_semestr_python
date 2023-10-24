

while True:
    try:
        a = int(input("введите первое число"))
        b = int(input("введите второе число"))
        c = int(input("введите третье число"))
        break
    except ValueError:
            print("что то пошло не так")
            continue

if a >= 0:
    a = True
else:
    a = False

if b >= 0:
    b = True
else:
    b = False

if c >= 0:
    c = True
else:
    c = False


if (a == True and b == False and c == False or a == False and b == True and c == False or a == False and b == False
        and c == True):
    print("одно из чисел положительное")
else:
    print("высказывание ложно")
