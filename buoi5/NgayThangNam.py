# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:08:02 2024

@author: mtpha
"""

thoi_gian =input("Nhập ngày tháng năm: ")
aa, bb, cccc = map(int, thoi_gian.split("/")) 

if cccc %4 == 0  and cccc %100 != 0 or cccc %400 == 0:
    kiem_tra = "Năm nhuận"
else:
    kiem_tra = "Năm không nhuận"
    
so_ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if kiem_tra:
    so_ngay[1] = 29

if aa < 1 or aa > so_ngay[bb-1]:
    print( "Ngày không hợp lệ")
elif bb < 1 or bb > 12:
   print( "Tháng không hợp lệ")
elif cccc < 1:
    print( "Năm không hợp lệ")
else:
    print( "Ngày tháng năm hợp lệ")
    
print("Xác định năm: ", kiem_tra)