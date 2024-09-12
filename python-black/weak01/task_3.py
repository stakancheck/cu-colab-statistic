#! /usr/bin/env python3
# Задача 3

income_count = int(input('Введите количество статей доходов: '))
expense_count = int(input('Введите количество статей расходов: '))

total_income = 0
total_expense = 0
balance = 0

for _ in range(income_count):
    income = int(float(input('Введите доход: ')) * 10)
    total_income += income
    balance += income

for _ in range(expense_count):
    expense = int(float(input('Введите расход: ')) * 10)
    total_expense += expense
    balance -=expense

if balance > 0:
    print('Положительный баланс')
else:
    print('Дефицит')
