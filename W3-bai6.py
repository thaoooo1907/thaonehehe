# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:43:14 2024

@author: LehiLamThuong-23722951
"""

n = int(input("Nhập số lần in chữ 'Hello': "))

if n < 1000:
    for _ in range(n):
        print("Hello")
else:
    print("Tham số phải nhỏ hơn 1000")