# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:25:59 2024

@author: LeThiLamThuong-23722951
"""

x = input("Nhập số nguyên x: ")
y = input("Nhập số nguyên y: ")
while True:
    if x.lstrip('-').isdigit() and y.lstrip('-').isdigit():
        x = int(x)
        y = int(y)
        if x > 0 and y > 0:
            break
        else:
            print("Cả hai số nguyên phải lớn hơn 0. Vui lòng nhập lại:")
    else:
        print("Vui lòng nhập các số nguyên hợp lệ:")
    x = input("Nhập số nguyên x: ")
    y = input("Nhập số nguyên y: ")
a, b = x, y
while b != 0:
    a, b = b, a % b
print("Ước chung lớn nhất của {} và {} là: {}".format(x, y, a))