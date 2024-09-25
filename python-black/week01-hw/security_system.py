#! /usr/bin/env python3
# week01
# Задача 4

door_locked = True
alarm_active = True

if door_locked:
    alarm_active = True
    print('Дверь заперта')
else:
    alarm_active = False
    print('Дверь не заперта')

if alarm_active:
    print('Сигнализация включена')
else:
    print('Сигнализация выключена')
