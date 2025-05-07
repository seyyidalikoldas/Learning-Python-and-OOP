numbers = [1,10,5,16,4,9,10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
#val = max(numbers)
#val = max(letters)
#val = min(letters)

#val = numbers [3:6]

numbers.append(49)
numbers.insert(3,78) #3.indexten hemen önceye sağındaki rakamı ekler
#numbers.pop() #son indexi siler
#numbers.pop(0) #ilk eleman silinir
print(numbers)
numbers.remove(49) #silmek istediğin indexi yaz arama yapıp siler

numbers.sort() #küçükten büyüğe sıralar
numbers.reverse() #sıralamayı ters çevirir
print(len(numbers))

print(numbers.counts(10)) #kaç tane 10 olduğunu söyler
numbers.clear() #bütün elemanları siler

