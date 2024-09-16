# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:53:56 2024

@author: LeThiLamThuong-23722951
"""

import math
values = [2, 4, 8, 16, 32, 64, 128]
width_n = 10
width_log_n = 10
width_n_log_n = 15
width_n_squared = 10
width_n_cubed = 10
print("n".ljust(width_n), end='\t')
print("log n".ljust(width_log_n), end='\t')
print("n log n".ljust(width_n_log_n), end='\t')
print("n^2".ljust(width_n_squared), end='\t')
print("n^3".ljust(width_n_cubed))
for n in values:
    log_n = math.log2(n)  
    n_log_n = n * log_n 
    n_squared = n ** 2   
    n_cubed = n ** 3     
    print(str(n).ljust(width_n), end='\t')
    print("{:.4f}".format(log_n).ljust(width_log_n), end='\t')
    print("{:.4f}".format(n_log_n).ljust(width_n_log_n), end='\t')
    print("{:.4f}".format(n_squared).ljust(width_n_squared), end='\t')
    print("{:.4f}".format(n_cubed).ljust(width_n_cubed))