#class
class Person:
    pass
    #class attributes

    #constructor (yapıcı metod)
    def __init__(self, name, year): #self: referansı tutar
    #object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
    #methods
    def intro(self):
        print('Hello There. I am ' + self.name) #ismide yazdırır
    
    def calculateAge(self):
        return 2023 - self.year

#object, instance
p1 = Person(name = "ali", year =1990) #ikisi de olur
p2 = Person("ahmet", 1995)

p1.intro()

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')

class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle() #yarıçapı 1
c2 = Circle(5)

print(f'c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')