#2. Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.

n = int(input())
sum_nums = 0
list_nums = []

for i in range(1, n + 1):
    result = round((1 + 1 / i) ** i)
    list_nums.append(result)
    sum_nums += result

print(list_nums)
print(sum_nums)
