# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:40:29 2024

@author: ADMIN
"""

a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))


while True:
    if a <= 0 or b <= 0 or c <= 0:
        print("Các cạnh phải là số nguyên dương.")
        a = int(input("Nhập lại cạnh thứ nhất: "))
        b = int(input("Nhập lại cạnh thứ hai: "))
        c = int(input("Nhập lại cạnh thứ ba: "))
        continue
    
    if a + b > c and a + c > b and b + c > a:
        break
    else:
        print("Ba cạnh không thể tạo thành một tam giác.")
        a = int(input("Nhập lại cạnh thứ nhất: "))
        b = int(input("Nhập lại cạnh thứ hai: "))
        c = int(input("Nhập lại cạnh thứ ba: "))

while True:
    if a == b == c:
        print("Tam giác đều")
        break
    elif a == b or b == c or a == c:
        
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            print("Tam giác cân và vuông")
        else:
            print("Tam giác cân")
        break
    else:
       
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
            print("Tam giác vuông")
        else:
            print("Tam giác thường")
        break
