# sayilar = [1,3,5,7,9,12,19,21]

# x=0

# while x<len(sayilar):
#     print(sayilar[x])
#     x+=1

# firstNum = int(input("İlk Numarayı Giriniz: "))
# lastNum = int(input("Son Numarayı Giriniz: "))

# while firstNum<lastNum:
#     if(firstNum%2==1):
#         print(firstNum)
#         firstNum+=1
#     else:
#         firstNum+=1

# x,y,z,k,l = int(input("Sayıları giriniz: "))

# total = [x,y,z,k,l]

# for a in total:
#     print(a)

number = int(input("Ürün sayısını giriniz: "))
x=0
urunler = []
while x<number:
    name = input(f"{x+1}.ürünün ismini yazın: ")
    price = int(input(f"{name} ürününün fiyatını giriniz: "))
    urunler.append({
        "name" : name,
        "price" : price
    })
    x+=1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']} ")