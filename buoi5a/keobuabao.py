# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:27:28 2024

@author: mtpha
"""

import random 
a=input("Nguoi choi:" )
chonlua = ["Kéo","Búa","Bao"]
b= random.choice(chonlua)
print("May chon:", b)

if a==b:
  print("Hoa")
elif a=="Kéo" and b=="Bao":
  print("Nguoi choi thang")  
elif a=="Búa" and b=="Kéo":
  print("Nguoi choi thang")
elif a=="Bao" and b=="Búa":
  print("Nguoi choi thang")  
else: 
  print("Nguoi may thang")