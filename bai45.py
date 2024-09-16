# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:49:27 2024

@author: ADMIN
"""

x = float(input("Nhập giá trị x: "))

n = int(input("Nhập số lượng số hạng n: "))

while n <= 0:
    print("Số lượng số hạng phải là số nguyên dương.")
    n = int(input("Nhập lại số lượng số hạng n: "))


tong = 0
mau = 0
i = 1
while i <= n:
    mau += i
    tong += x ** i / mau
    i += 1


print("Tổng của dãy số là:", tong)
