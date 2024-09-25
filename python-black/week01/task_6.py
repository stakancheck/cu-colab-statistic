#! /usr/bin/env python3
# Задача 6

side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('Можно')
else:
    print('Нельзя')
