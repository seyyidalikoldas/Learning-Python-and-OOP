import random
a=0
b=0

random=random.randint(1,100)
puan=100

while a<1:
    x = int(input("1 ile 100 arasında bir sayı giriniz: "))
    y = int(input("Hak sayısını giriniz: "))
    a+=1
    if (random==x):
        print("Tebrikler Bildiniz")

    else:
        print("Hatalı sayı girdiniz: ")
        while b<1:
            play = input("Aşağı mı Yukarı mı: ")
            if play=="aşağı":
                x = x+1
                if x==random:
                    print("Doğru Bildiniz")
            elif play=="yukarı":
                x = x-1
                if x==random:
                    print("Doğru Bildiniz")