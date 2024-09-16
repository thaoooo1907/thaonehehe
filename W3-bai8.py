# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:49:27 2024

@author: LeThiLamThuong-23722951
"""

import random
import sys
if len(sys.argv) != 2:
    print("Vui lòng nhập một số nguyên n.")
else:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Tham số nhập vào không phải là số nguyên.")
    else:
        if n <= 0:
            print("Số nguyên n phải lớn hơn 0.")
        else:
            numbers = [random.random() for _ in range(n)]
            avg = sum(numbers) / n
            min_value = min(numbers)
            max_value = max(numbers)
            print("Giá trị trung bình:", "%.4f" % avg)
            print("Giá trị nhỏ nhất:", "%.4f" % min_value)
            print("Giá trị lớn nhất:", "%.4f" % max_value)