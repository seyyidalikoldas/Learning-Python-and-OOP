mylist = [1,2,3]
myString = "My String"

print(len(mylist))
print(len(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie created")
        
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration

m = Movie("The Matrix", "Wachowski", 136)
print(m)
print(len(m))