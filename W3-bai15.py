# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:08:07 2024

@author: LeThiLamThuong-23722951
"""
i = int(input("Nhập số nguyên i: "))
k = int(input("Nhập cơ số k (từ 2 đến 16): "))
if k < 2 or k > 16:
    print("Cơ số k phải nằm trong khoảng từ 2 đến 16.")
else:
    digits = "0123456789ABCDEF"
    result = ""
    if i == 0:
        result = "0"
    else:
        while i > 0:
            result = digits[i % k] + result
            i //= k
    print("Số trong cơ số {} là: {}".format(i, result))
