# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:15:49 2019

@author: Iakunin.Sergey
"""
import hashlib


password = hashlib.sha256('DeadBeaf'.encode()).hexdigest()
line = input('Enter password: ')
encoded_line = hashlib.sha256(line.encode()).hexdigest()
if password == encoded_line:
    print('OK')
else:
    print('Not OK, go away')