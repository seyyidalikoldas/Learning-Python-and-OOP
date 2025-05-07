name = input("Bir kelime giriniz: ")
number = int(input("Bir sayı giriniz: "))
def function(name,number):
    for i in range(number):
        print(name)

function(name,number)

number1 = int(input("Bir sayı giriniz: "))
number2 = int(input("Bir sayı giriniz: "))

def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

liste = listeyeCevir(10,20,30,"Merhaba",40,50,60,70,80,90,100)
print(liste) 



def function1(number1,number2):
    for sayi in range(number1, number2+1):
        if sayi>1:
            for i in range(2, sayi):
                if (sayi%i==0):
                    break
            else:
                print(sayi) # sayi asal sayıdır
        
    
function1(number1,number2)



def tamBolen(sayi):
    tamBolenler = []
    for i in range(2, sayi):
        if sayi%i==0:
            tamBolenler.append(i)
    return tamBolenler

print(tamBolen(20))