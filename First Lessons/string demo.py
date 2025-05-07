website = "http://www.sadikturan.com"
course = "Pyhton Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

q1 = str(len(course))
print(q1)

q2 = website[7:10]
print(q2)

lengthWebsite = len(website)
q3 = website[lengthWebsite-3:]
print(q3)

q4 = course[:15] + course[-15:]
print(q4)

q5 = course[::-1]

name, surname, age, job = "Bora" , "Yılmaz", 32, "mühendis"

print(f"Benim adım {name} {surname} Yaşım {age} ve mesleğim {job}.")

a = "Hello world"
a = a[0:6] + "W" +a[7:] #ya da a.replace("w","W")

print(a)


b="abc"
q8 = b*3
print(q8)
