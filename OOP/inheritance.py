# Inheritance (Kalıtım): Bir sınıfın başka bir sınıftan özelliklerini almasıdır.

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person) => name, lastname, age, eat(), run(), drink(), school, exam(), do_homework()
# Teacher(Person) => name, lastname, age, eat(), run(), drink(), branch, give_exam(), make_document()

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person): 
    def __init__(self, fname, lname, number):
        self.studentNumber = number
        Person.__init__(self, fname, lname) #Person classının init metodunu çalıştırır
        print("Student Created")
        print(self.firstName)
        print(self.studentNumber)

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) #self yazmaya gerek yok
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Ali", "Yılmaz")
s1 = Student("Can", "Yılmaz", 1256)
t1 = Teacher("Serkan", "Yılmaz", "Math")
p1.eat()
s1.eat()
p1.who_am_i()
s1.who_am_i()
t1.who_am_i()