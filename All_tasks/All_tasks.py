# Задача 2: Найдите сумму цифр трехзначного числа.

digit_three = int(input('Введите трехзначное число '))
if digit_three < 1000 and digit_three > 99:
    print((digit_three % 10) + ((digit_three // 10) % 10) + (digit_three // 100))
elif digit_three > -1000 and digit_three < -99:
    print(((digit_three * -1) % 10) + (((digit_three * -1) // 10) % 10) + ((digit_three * -1) // 100))
else: 
    print('Введенное число не трехзначное')



    # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


crane_bird = int(input("Сколько журавликов всего сделали дети? "))
if crane_bird % 6 == 0:
    bird_Petr = crane_bird // 6
    bird_Sergey = crane_bird // 6
    bird_Kate = (bird_Petr + bird_Sergey) * 2
    print(f'{bird_Petr} - {bird_Kate} - {bird_Sergey}')
else: print('При колличестве журавликов не кратных 6 в целых числах ответ выдать невозможно')



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number_ticket = int(input('Введите номер вашего билета '))

if number_ticket < 1000000 and number_ticket > 99999:
    first_number_ticket = number_ticket // 1000
    second_sum = 0
    while number_ticket > 1000:
        second_sum = second_sum + (number_ticket % 10)
        number_ticket = number_ticket // 10
    first_sum = 0
    while first_number_ticket < 1000 and first_number_ticket > 0:
        first_sum = first_sum + (first_number_ticket % 10)
        first_number_ticket = first_number_ticket // 10
    if second_sum == first_sum:
        print('У вас счастливый билет!')
    else:
        print('Вам не повезло :(')
else: 
    print('В вашем билете должно быть шесть цифр!!!')



    # Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_length = int(input('Введите длину шоколадки в дольках '))
chocolate_width = int(input('Введите ширину шоколадки в дольках '))
slice_chocolate = int(input('Сколько долек вы хотите отломить? '))

if slice_chocolate % chocolate_length == 0 or slice_chocolate % chocolate_width == 0:
    print('При таком колличестве долек вы можете разделить шоколадку на два прямоугольника одним разломом')
else:
    print('При таком колличестве долек вы не можете разделить шоколадку на два прямоугольника одним разломом')