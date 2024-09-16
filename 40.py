# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:42:15 2024

@author: ADMIN
"""

n = int(input("Nhập số lượng số hạng n: "))

while n <= 0:
    print("Số lượng số hạng phải là số nguyên dương.")
    n = int(input("Nhập lại số lượng số hạng n: "))

tong = 0
i = 1
while i <= n:
    mau = 2 * i
    tong += 1 / mau
    i += 1

print("Tổng của dãy số là:", tong)
