# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:04:15 2024

@author: ADMIN
"""

km = float(input("Nhập số km đi: "))


while km < 0:
    print("Số km không thể là số âm. Vui lòng nhập lại.")
    km = float(input("Nhập số km đi: "))

total_cost = 0.0

if km > 0:
    total_cost += 15000  

if km > 1:
    if km <= 5:
        total_cost += (km - 1) * 13500
    else:
        total_cost += 4 * 13500  

if km > 5:
    total_cost += (km - 5) * 11000  

if km > 120:
    total_cost *= 0.90  


print(f"Tổng tiền cước taxi là: {total_cost:.0f}đ")
