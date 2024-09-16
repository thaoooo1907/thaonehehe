# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:37:18 2024

@author: ADMIN
"""

import random

options = ["Kéo", "Búa", "Bao"]


while True:
    
    user_choice = input("Nhập lựa chọn của bạn (Kéo, Búa, Bao) hoặc 'thoat' để dừng: ").capitalize()
    
    if user_choice == 'Thoat':
        print("Cảm ơn bạn đã chơi!")
        break
    
    if user_choice not in options:
        print("Lựa chọn không hợp lệ. Vui lòng nhập 'Kéo', 'Búa', hoặc 'Bao'.")
        continue
    
    computer_choice = random.choice(options)
    print(f"Máy tính chọn: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "Hòa"
    elif (user_choice == "Kéo" and computer_choice == "Bao") or \
         (user_choice == "Búa" and computer_choice == "Kéo") or \
         (user_choice == "Bao" and computer_choice == "Búa"):
        result = "Bạn thua"
    else:
        result = "Bạn thắng"
    
    print(result)
