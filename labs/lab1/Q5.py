veri1 = int(input())
veri2 = int(input())
veri3 = int(input())

if veri1 < veri2 + veri3 and veri2 < veri1 + veri3 and veri3 < veri1 + veri2:
  print("True")
else:
  print("False")
