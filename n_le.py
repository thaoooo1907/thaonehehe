# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:02:28 2024

@author: ADMIN
"""


while True:
    try:
        n = int(input("Nhập số lẻ và lớn hơn 0 n: "))
        if n > 0 and n % 2 != 0:
            break
        else:
            print("Số nhập vào phải là số lẻ và lớn hơn 0. Vui lòng nhập lại.")
    except ValueError:
        print("Đầu vào không phải là số nguyên. Vui lòng nhập lại.")

tich = 1
i = 1
while i <= n:
    tich *= i
    i += 1
print(f"Tích S = 1 × 2 × 3 × ... × {n} là: {tich}")
