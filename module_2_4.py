numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    is_prime = True
    if number > 1:
        for number_1 in range(2, number):
            if (number % number_1) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        else:
            not_primes.append(number)
    else:
        not_primes.append(number)


print(f"Простые числа: {primes}")
print(f"Не простые числа: {not_primes}")

