number = int(input('Введите число: '))
result = []
for i in range(1, number):
    for j in range(i + 1, number):
        if number % (i + j) == 0:
            result.append(i)
            result.append(j)
        else:
            continue

print(*result)




