# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:12:28 2024

@author: LeThiLamThuong-23722951
"""

n = input("Nhập một số nguyên dương: ")
while True:
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Số nguyên phải lớn hơn 0. Vui lòng nhập lại:")
    else:
        print("Vui lòng nhập một số nguyên hợp lệ:")
    n = input()
B = bin(n)[2:]
print("Biểu diễn nhị phân của số là:",B)