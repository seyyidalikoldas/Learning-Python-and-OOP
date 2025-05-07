website = "http://www.sadikturan.com"
course = "Pyhton Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#Q1

a = " Hello World "
a = a.strip()
print (a)

#Q2

index = website.find("sadikturan")
index2 =website.find(".com")
b = website[index:index2]
print(b)

#Q3

c = course.lower()
print(c)

#Q4

d = website.count("a")
print(d)

#Q5

e = website.startswith("ww") & website.endswith("com")
print(e)

#Q6

f = website.find(".com")
print(f)

#Q7

g = course.isalpha()
print(g)

#Q8

h = "Contents"
h = h.center(50,"*")
print(h)

#Q9

j = course.replace(" " , "-")
print(j)

#Q10

k = "Hello World"
k = k.replace("World" , "There")
print(k)

#Q11

l = course.split()
print(l)


