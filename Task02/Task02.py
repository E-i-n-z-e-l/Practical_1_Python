# Задача 2: Найдите сумму цифр трехзначного числа.

digit_three = int(input('Введите трехзначное число '))
if digit_three < 1000 and digit_three > 99:
    print((digit_three % 10) + ((digit_three // 10) % 10) + (digit_three // 100))
elif digit_three > -1000 and digit_three < -99:
    print(((digit_three * -1) % 10) + (((digit_three * -1) // 10) % 10) + ((digit_three * -1) // 100))
else: 
    print('Введенное число не трехзначное')



# Решение через цикл while
# count = 0
# sum = 0
# while count <= 3:
#     sum = sum + digit_three % 10
#     digit_three = digit_three // 10
#     count = count + 1





