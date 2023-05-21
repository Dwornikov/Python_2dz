S = int(input('Введите сумму чисел S: '))
P = int(input('Введите произведение чисел P: '))

found = False

for X in range(1, S):
    Y = S - X
    if X * Y == P:
        found = True
        break

if found:
    print("Задуманные числа:", X, Y)
else:
    print("Числа не найдены.")
