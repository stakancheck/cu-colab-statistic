#! /usr/bin/env python3
# Задача 4

# напиши программу, которая считывает два числа и выполняет арифметические операции с ними: сумму, разность, произведение и деление — а затем выводит результаты.

number1 = int(input())
number2 = int(input())

num_sum = number1 + number2
num_difference = number1 - number2
num_product = number1 * number2
num_division = number1 / number2

print(num_sum, num_difference, num_product, num_division)
