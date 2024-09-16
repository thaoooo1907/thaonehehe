# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:35:40 2024

@author: ADMIN
"""

import re

# Kiểm tra ID người dùng
user_id = input("Nhập ID User: ")

while True:
    # Kiểm tra độ dài ID
    if len(user_id) < 6 or len(user_id) > 24:
        print("ID User phải có từ 6 đến 24 ký tự.")
    # Kiểm tra ký tự không hợp lệ
    elif re.search(r'[!@#$%^&*()\-+=]', user_id):
        print("ID User không được chứa các ký tự: ! @ # $ % ^ & * ( ) - = +")
    # Kiểm tra khoảng trắng
    elif ' ' in user_id:
        print("ID User không được chứa khoảng trắng.")
    else:
        break  # ID hợp lệ
    user_id = input("Nhập lại ID User: ")

# Kiểm tra mật khẩu
password = input("Nhập Password: ")

while True:
    # Kiểm tra độ dài mật khẩu
    if len(password) < 6 or len(password) > 24:
        print("Password phải có từ 6 đến 24 ký tự.")
    # Kiểm tra ít nhất 1 chữ cái thường
    elif not re.search(r'[a-z]', password):
        print("Password phải chứa ít nhất 1 chữ cái thường.")
    # Kiểm tra ít nhất 1 số
    elif not re.search(r'[0-9]', password):
        print("Password phải chứa ít nhất 1 số.")
    # Kiểm tra ít nhất 1 chữ cái hoa
    elif not re.search(r'[A-Z]', password):
        print("Password phải chứa ít nhất 1 chữ cái hoa.")
    # Kiểm tra ít nhất 1 ký tự đặc biệt
    elif not re.search(r'[$#@]', password):
        print("Password phải chứa ít nhất 1 ký tự đặc biệt trong [$ # @].")
    else:
        break  # Mật khẩu hợp lệ
    password = input("Nhập lại Password: ")

print("Đăng nhập thành công!")
