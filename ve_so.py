# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:23:01 2024

@author: ADMIN
"""

import random

n = int(input("Nhập số lượng vé số mua: "))

while n <= 0:
    print("Số lượng vé phải là số nguyên dương.")
    n = int(input("Nhập lại số lượng vé số mua: "))

tickets = []
for _ in range(n):
    ticket = set()
    while len(ticket) < 6:
        number = int(input("Nhập một số từ 1 đến 45: "))
        if 1 <= number <= 45:
            ticket.add(number)
        else:
            print("Số nhập vào không hợp lệ. Vui lòng nhập lại.")
    tickets.append(ticket)

winning_numbers = set(random.sample(range(1, 46), 6))

print(f"Dãy số trúng thưởng là: {sorted(winning_numbers)}")

total_prize = 0
for ticket in tickets:
    match_count = len(ticket & winning_numbers)
    if match_count == 3:
        total_prize += 30000
    elif match_count == 4:
        total_prize += 300000
    elif match_count == 5:
        total_prize += 10000000
    elif match_count == 6:
        total_prize += 10000000000

print(f"Tổng số tiền người chơi nhận được là: {total_prize} đ")
