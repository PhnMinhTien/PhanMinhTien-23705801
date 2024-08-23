a = float(input("Nhap canh a:"))
b = float(input("Nhap canh b:"))
c = float(input("Nhap canh c:"))
if (a+b)>c or (a+c)>b or (b+c)>a:
    print ("Day la tam giac thuong")
    if a == b == c:
        print ("Day la tam giac deu");
    elif a == b or b == c or c == a:
      print ("Day la tam giac can")
    elif (a*a+b*b==c*c) or (b*b+c*c==a*a) or (c*c+a*a==b*b):
      print ("Day la tam giac vuong")

  
else:
   print("Đây không phải là tam giác")
