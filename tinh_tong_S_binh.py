# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:14:18 2024

@author: ADMIN
"""

n = int(input("Nhập số nguyên dương n: "))


while n <= 0:
    print("Số nhập vào phải là số nguyên dương.")
    n = int(input("Nhập lại số nguyên dương n: "))

i = 1
S = 0

while i <= n:
    S += i * i
    i += 1
print(f"Tổng S = 1^2 + 2^2 + ... + {n}^2 là: {S}")
