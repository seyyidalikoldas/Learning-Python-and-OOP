# def square(num): return num **2

numbers = [1,3,5,9]

result = list(map(lambda num: num **2, numbers))

# #lambda ifadesinin genel sözdizimi şu şekildedir:

# python
# Copy code
# lambda arguments: expression
# Burada:

# arguments: Lambda fonksiyonunun parametreleri.
# expression: Parametreleri kullanarak geri döndüreceği sonuç ifadesi.
# Lambda fonksiyonları genellikle map(), filter(), reduce() gibi fonksiyonlarla kullanılır veya başka bir fonksiyonun içinde geçici olarak tanımlanıp kullanılır. Özellikle kısa işlemler yapmak için ve kodun okunurluğunu artırmak için tercih edilirler.

# Örnek olarak, lambda ifadesini kullanarak basit bir toplama işlemi yapan bir fonksiyon oluşturabiliriz:

# python
# Copy code
# add = lambda x, y: x + y
# result = add(3, 5)
# print(result)  # Çıktı: 8
# Aynı işlemi normal bir fonksiyonla da yapabiliriz:

# python
# Copy code
# def add(x, y):
#     return x + y

# result = add(3, 5)
# print(result)  # Çıktı: 8
# Lambda ifadesinin avantajı, tek satırda basit işlemleri tanımlayabilmemiz ve daha az yazı ile aynı işi yapabilmemizdir. Ancak, daha karmaşık fonksiyonlar için lambda ifadesi kullanmak yerine normal fonksiyon tanımlamak daha okunaklı olabilir.

# result = square(2)

# for item in map(square, numbers):
#     print(item)

print(result)