#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:00:28 2023

@author: ws3
"""

import secrets
import string

let = string.ascii_letters
digi = string.digits
spl_char  = string.punctuation



password = let + digi + spl_char

pass_len = 8

# Use a list  store the characters of the password
pass_list = []

for i in range(pass_len):
    pass_list.append(secrets.choice(password))

password_str = ''.join(pass_list)

print(password_str)
