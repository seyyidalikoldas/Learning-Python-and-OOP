# # sayi = int(input("sayı: "))

# # if (0<sayi<100):
# #     print(f"{sayi} sayısı 0 ile 100 arasındadır.")

# # if (sayi%2 == 0):
# #     print(f" {sayi} sayısı çifttir")
# # else:
# #     print(f"{sayi} sayısı tektir")

# email = "a@mail"
# password = "a123"

# inputMail = input("Maili Giriniz: ")
# inputPassword = input("Şifreyi Giriniz: ")

# if(email == inputMail) and (password==inputPassword):
#     print("Hoş Geldiniz")
# elif(email == inputMail):
#     print("Şifre hatalı")
# elif(password==inputPassword):
#     print("Mail Hatalı")


# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if(b<a) and (a>c):
#     print("a en büyük sayıdır")
# elif(b>c):
#     print("b en büyük sayıdır")
# elif(c>a):
#     print("c en büyük sayıdır")
# else:
#     print("Eşit rakamlar vardır")

vize1 = float(input("Vize1 notunu giriniz: "))
vize2 = float(input("Vize2 notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

vizetotal = (vize1+vize2)/2
total = vizetotal*60/100 +final*40/100

if(final>=50) and (total>=50):
    print("Dersi Geçtiniz")
elif(final>=50):
    print("Ortalamanız 50 altında")
elif(total>=50):
    print("Final notunuz 50 altında")
