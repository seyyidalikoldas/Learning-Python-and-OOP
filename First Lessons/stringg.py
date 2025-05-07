name = "Ali"
surname = "Koldaş"
age = 18
greeting = "My name is: " + name + " Surname: " +surname + " \nAge: " +str(age)
length = len(greeting)
print(greeting[0])
print(greeting[3])
print(greeting[length-1]) #son harfi yazdırır
print(greeting[-1]) #son harfi yazdırır
print(greeting[3:7]) #3.indexten 7.ye kadar
print(greeting[3:]) #3ten sona kadar
print(greeting[:16]) #baştan 16ya kadar
print(greeting[2:40:2]) #2den 40a kadar ancak 2şer 2şer yazdırır yani 2 harfte 1 harf yazdırır
