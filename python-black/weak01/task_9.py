#! /usr/bin/env python3
# Задача 9

import sys

num_sum = 0
num_count = 0

for line in sys.stdin:
    if line.strip() == '':
        break
    num_sum += int(line.strip())
    num_count += 1


print(num_sum, num_sum / (num_count + 1))
