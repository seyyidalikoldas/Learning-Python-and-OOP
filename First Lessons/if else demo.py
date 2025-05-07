name = input("İsminizi Giriniz: ")
age = int(input("Yaşınızı Giriniz: "))
education = input("Eğitim Bilginizi Giriniz: ")

if (age<18):
   print(f"Sayın {name} Yaşınız 18'den küçük.")

elif(education=="Lise") or (education=="Üniversite"):
    print(f"Sayın {name} Ehliyet Almaya Hak Kazandınız")

else :
    print(f"Sayın {name} Eğitim Durumunuz İzin Vermiyor")

yazili1 = int(input("1.Yazılı Notunu Giriniz: "))
yazili2 = int(input("2.Yazılı Notunu Giriniz: "))
sozlu = int(input("Sözlü Notunu Giriniz: "))


ort = (yazili1 + yazili2 + sozlu)/3

if ort<25:
    print(0)
elif ort<45:
    print(1)
elif ort<55:
    print(2)
elif ort<70:
    print(3)
elif ort<85:
    print(4)
elif ort<=100:
    print(5)

days = int (input ("aracınız kaç gündür trafikte"))


if days<=365:
   print("1 Yıl")
elif days<=730:
    print("2 Yıl")
else:
    print("3 Yıl")

import datetime

tarih = input("aracınız ne zaman alındı (2021/8/9):  ")
tarih = tarih.split("/")
print(tarih[0])
print(tarih[1])
print(tarih[2])

tarih = datetime.datetime(int(tarih[0]) , int(tarih[1]) , int(tarih[2]) )

simdi = datetime.datetime.now()

fark = simdi -tarih
print(fark)

