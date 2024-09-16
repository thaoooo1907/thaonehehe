# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:27:21 2024

@author: ADMIN
"""

import re

valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]

email = input("Nhập địa chỉ email: ")

while True:

    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        local_part, domain_part = email.split('@')
        
       
        if len(local_part) >= 6 and ' ' not in local_part and not re.search(r'[!#$%^&*()+=\[\]{};:\'",<>?/\\|]', local_part):
            domain = domain_part.lower()
            if domain in valid_domains:
                print("Địa chỉ email hợp lệ.")
                break
            else:
                print("Tên miền không hợp lệ. Vui lòng nhập lại.")
        else:
            print("Phần trước ký tự '@' không hợp lệ. Vui lòng nhập lại.")
    else:
        print("Địa chỉ email không hợp lệ. Vui lòng nhập lại.")
    
    
    email = input("Nhập lại địa chỉ email: ")
