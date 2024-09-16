# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:45:46 2024

@author: ADMIN
"""

import random

options = ["Kéo", "Búa", "Bao"]

num_players = random.randint(8, 20)
print(f"Số lượng người chơi: {num_players}")

choices = []

i = 0
while i < num_players:
    choices.append(random.choice(options))
    i += 1
print("Lựa chọn của các người chơi:")
for idx, choice in enumerate(choices):
    print(f"Người chơi {idx + 1}: {choice}")

i = 0
while i < num_players:
    j = i + 1
    while j < num_players:
        choice1 = choices[i]
        choice2 = choices[j]
        
        if choice1 == choice2:
            result = "Hòa"
        elif (choice1 == "Kéo" and choice2 == "Bao") or \
             (choice1 == "Búa" and choice2 == "Kéo") or \
             (choice1 == "Bao" and choice2 == "Búa"):
            result = f"Người chơi {i + 1} thắng"
        else:
            result = f"Người chơi {j + 1} thắng"
        
        print(f"Cuộc đối đầu giữa người chơi {i + 1} ({choice1}) và người chơi {j + 1} ({choice2}): {result}")
        j += 1
    
    i += 1
