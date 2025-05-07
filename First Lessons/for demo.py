sayilar = [1,3,5,7,9,12,19,21]

# for i in sayilar:
#     if(i%3==0):
#         print(i)

# total = 0
# for j in sayilar:
#     total+=j

# print(total)

# for i in sayilar:
#     if(i%2==1):
#         print(i**2)

# sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize",]

# for a in sehirler:
#     if(len(a)<=5):
#         print(a)
totalprice=0

urunler = [
    {"name" : "samsung s6", "price" : "3000"},
    {"name" : "samsung s7", "price" : "4000"},
    {"name" : "samsung s8", "price" : "5000"},
    {"name" : "samsung s9", "price" : "7000"},
]
    

# for a in urunler:
#   totalprice+=int(a["price"]) 



# print(totalprice)
for a in urunler:
    if int(a["price"]) <=5000:
        print(a["name"])



