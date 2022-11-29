#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from ipaddress import summarize_address_range


n = float(input("Введите вещественное число: \n"))
sum_digits = 0

a = len(str(n)) - 2
n *= 10 ** a

while n:
    sum_digits += n % 10
    n //= 10

print(int(sum_digits))