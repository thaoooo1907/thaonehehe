# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:59:41 2024

@author: ADMIN
"""


n = int(input("Nhập số nguyên dương n: "))

while n <= 0:
    print("Số nhập vào phải là số nguyên dương.")
    n = int(input("Nhập lại số nguyên dương n: "))

is_prime = True

if n == 1:
    is_prime = False
else:

    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
