# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:44:35 2024

@author: mtpha
"""

a = float(input("Nhập số km: "))
So_tien_la = 0
if a <= 1 :
    So_tien_la = 20000
elif a <= 3 :
    So_tien_la = (a - 1 ) * 13000
elif a <=8:
    So_tien_la = 3 * 13000 + ( a - 3) * 12000
else:
    So_tien_la = 3 * 13000 + (a - 3) * 12000 + ( a - 8 ) * 10000
if So_tien_la > 100000:
    So_tien_la = (3 * 13000 + (a - 3) * 12000 + ( a - 8 ) * 10000) * 0.92
print("Tong tien: ",int(So_tien_la))