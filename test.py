#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:52:09 2020

@author: michelmake
"""


from rotate import Element


conn = [1, 2, 3, 4]
rng = [1, 2, 3, 4]

element = Element(conn, rng)

print('Original Element:')
print(conn)
print('Rotated Element Element:')
print(element.rotate(1))


