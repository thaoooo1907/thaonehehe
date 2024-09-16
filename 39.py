# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:38:16 2024

@author: ADMIN
"""

n = int(input("Nhập  n: "))

while n <= 0:
    print("Số lượng số hạng phải là số nguyên dương.")
    n = int(input("Nhập lại số  n: "))

tong = 0
i = 1
while i <= n:
    tong += 1 / i
    i += 1

print("Tổng của dãy số là:", tong)
