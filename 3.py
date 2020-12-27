n = int(input('Введите любое целое число - '))

if n < 0:
    n = -n
    n = str(n)
    min_two = n + n
    min_third = n + n + n
    min_two = int(min_two)
    min_third = int(min_third)
    two = -min_two
    third = -min_third
    n = int(n)
    n = -n
else:
    n = str(n)
    two = n + n
    third = n + n + n
print(f"{n} + {two} + {third} = {int(n) + int(two) + int(third)}")




