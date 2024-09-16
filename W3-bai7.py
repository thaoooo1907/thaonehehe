# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:47:37 2024

@author: LeThiLamThuong-23722951
"""

start = 1000
end = 2000
numbers_per_line = 5
count = 0
for i in range(start, end):
    print(i, end=" ")
    count += 1

    if count % numbers_per_line == 0:
        print()