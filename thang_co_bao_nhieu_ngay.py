# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:05:42 2024

@author: ADMIN
"""

month = int(input("Nhập tháng (1-12): "))
year = int(input("Nhập năm: "))

while month < 1 or month > 12:
    print("Tháng phải nằm trong khoảng từ 1 đến 12.")
    month = int(input("Nhập lại tháng (1-12): "))


while year <= 0:
    print("Năm phải là số nguyên dương.")
    year = int(input("Nhập lại năm: "))

days_in_month = 31  


if month in [4, 6, 9, 11]:
    days_in_month = 30
elif month == 2:
    
    is_leap_year = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap_year = True
    days_in_month = 29 if is_leap_year else 28


print(f"Tháng {month} năm {year} có {days_in_month} ngày.")
