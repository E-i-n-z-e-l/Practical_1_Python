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





