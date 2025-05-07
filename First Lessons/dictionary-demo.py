

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
tel = input("Öğrenci telefonu: ")

ogrenciler = {
   number : {
        "ad" : name,
        "soyad" : surname,
        "tel" : tel
    }
}
print(ogrenciler)
