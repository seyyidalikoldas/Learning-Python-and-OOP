def sayHello(name = "User"):
    return "Hello " + name
            
msg = sayHello("Ali")
print(msg)
sayHello()

def yasHesaapla(dogumYili):
    return 2023 - dogumYili
ageAli = yasHesaapla(2002)
ageBetul = yasHesaapla(2005)
ageUmmu = yasHesaapla(1999)
print(ageAli, ageBetul, ageUmmu)