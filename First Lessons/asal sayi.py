sayi = int(input("Bir sayi giriniz: "))
a = 2
asalmi = True
if sayi==1:
    print("Sayi asal değildir")
for i in range(2, sayi):
    if sayi%i==0:
        asalmi = False
        break
if asalmi:
    print("Sayi asaldır")
else:
    print("Sayi asal değildir")

    
    