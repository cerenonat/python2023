veri1 = input()
veri2 =  input()
veri3 = input()

if veri2.isdigit() and veri1.isdigit() and veri3.isdigit():
    if veri2 < veri1 < veri3 or veri3 < veri1 < veri2:
      print("True")
    else:
        print("False")
else:
    print("False")
   
