def changeName(n):
    n = "ada"

name = "ali"

changeName(name)

print(name) # ali

def change(n):
    n[0] = "istanbul"

sehirler = ["ankara", "izmir"]
n=sehirler[:] # [:] ile kopyalama yapılır   
n[0] = "istanbul"

print(n) # ['istanbul', 'izmir']

print(sehirler) # ['istanbul', 'izmir']     
change(sehirler[:])
print(sehirler) # ['ankara', 'izmir']   


def add(a, b,c=0): #bu şekilde varsayılan değer atayabiliriz ancak 5 tane ile sınırlı olur
    return sum((a,b,c))

add(10,20) # 30
print(add(10,20)) # 30

def add(*params): # * ile istediğimiz kadar parametre alabiliriz
    return sum((params))
print(add(10,20,30,40,50,60)) # 210


def displayUser(**args): # ** ile istediğimiz kadar parametre alabiliriz
    print(type(args)) # <class 'dict'> bu şekilde tipini öğreniriz
    for key, value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Ali", age = 2, city = "istanbul") # fonksiyonu tanımlamadan çağırdık    
displayUser(name = "Betül", age = 12, city = "Ankara", phone = "123456") # fonksiyonu tanımlamadan çağırdık
displayUser(name = "Ahmet", age = 22, city = "Mersin", phone = "123456", email ="ahmet@mail.com")

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50, key1 = "value 1", key2 = "value 2") # 10 20 (30, 40, 50) {'key1': 'value 1', 'key2': 'value 2'}
