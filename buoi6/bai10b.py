chuoi = "Đại học Quốc gia,Khu phố 6,P.Linh Trung,Q.Thủ Đức,Tp.HCM"
sub_strings = (sub.replace("P.", "").replace("Q.", ""). replace("Tp.", "") for sub in chuoi.split(","))
for sub in sub_strings:
   print(sub)
