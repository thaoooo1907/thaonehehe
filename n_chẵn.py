# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:00:44 2024

@author: ADMIN
"""

while True:
    try:
        n = int(input("Nhập số chẵn và lớn hơn 0 n: "))
        if n > 0 and n % 2 == 0:
            break
        else:
            print("Số nhập vào phải là số chẵn và lớn hơn 0. Vui lòng nhập lại.")
    except ValueError:
        print("Đầu vào không phải là số nguyên. Vui lòng nhập lại.")


tong = 0
i = 2
while i <= n:
    tong += i
    i += 2

print(f"Tổng S = 2 + 4 + 6 + ... + {n} là: {tong}")
