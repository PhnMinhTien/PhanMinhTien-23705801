import math
a, b = map(int,input("Nhập vào 2 số bất kì:").split())
D=(math.sqrt(a) - math.sqrt(b))/((a**0.25)-(b**0.25))
E=((a**0.5)+((a*b)**0.25))/((a**0.25)+(b**0.25))
F=D-E
print("Đáp án là: ",F )