# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:50:59 2024

@author: ADMIN
"""

import math

n = int(input("Nhập số nguyên dương n: "))

while n <= 0:
    print("Số nhập vào phải là số nguyên dương.")
    n = int(input("Nhập lại số nguyên dương n: "))


i = 1
is_perfect_square = False

while i * i <= n:
    if i * i == n:
        is_perfect_square = True
        break
    i += 1

if is_perfect_square:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
