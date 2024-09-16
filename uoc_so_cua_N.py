# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:16:49 2024

@author: ADMIN
"""

N = int(input("Nhập số nguyên dương N: "))

while N <= 0:
    print("Số nhập vào phải là số nguyên dương.")
    N = int(input("Nhập lại số nguyên dương N: "))

i = 1
print(f"Các ước số của {N} là:")
while i <= N:
    if N % i == 0:
        print(i, end=' ')
    i += 1
