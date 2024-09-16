# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:02:15 2024

@author: LenThiLamThuong-23722951
"""

a = 0
b = 1
count = 0
n = 100
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print()
