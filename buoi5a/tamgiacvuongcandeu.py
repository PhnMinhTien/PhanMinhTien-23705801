# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:19:40 2024

@author: mtpha
"""

a = float(input("Nhap canh a:"))
b = float(input("Nhap canh b:"))
c = float(input("Nhap canh c:"))
if (a+b)>c or (a+c)>b or (b+c)>a:
  print ("Day la tam giac");
else:
  print ("Day khong phai la tam giac");