# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def xep_hang_hoc_luc(gpa):
    if gpa < 3.5:
        return "Học lực Kém"
    elif 3.5 <= gpa < 5.0:
        return "Học lực Yếu"
    elif 5.0 <= gpa < 7.0:
        return "Học lực Trung bình"
    elif 7.0 <= gpa < 8.0:
        return "Học lực Khá"
    elif 8.0 <= gpa < 9.0:
        return "Học lực Giỏi"
    elif 9.0 <= gpa <= 10:
        return "Học lực Xuất sắc"



gpa = float(input("Nhập điểm GPA: "))


xep_hang = xep_hang_hoc_luc(gpa)


print("GPA:", gpa, "Xếp hạng học lực : ", xep_hang)