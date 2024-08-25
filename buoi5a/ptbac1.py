# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:09:18 2024

@author: mtpha
"""

a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
if a == 0:
  if b == 0:
    print("Phuong trinh vo so nghiem")
  else:
    print("Phuong trinh vo nghiem")
else:
  x = -b/a
print("Phuong trinh co nghiem la:", x)
