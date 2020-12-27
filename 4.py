num1 = int(input('Введите целое положительное число - '))
while num1 < 0:
    num = int(input('Введите целое ПОЛОЖИТЕЛЬНОЕ число - '))
max = 0
num = num1
while num > 0:
    dig = num % 10
    if dig > max:
        max = dig
    if dig == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num1} - {max}")


