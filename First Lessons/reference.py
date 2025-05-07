#value type

x=5
y=25
x=y
y=10
print(x,y)


#reference types => list

a=["1" , "2"]
b=["1", "2"]

a=b

b[0] = "grape"

print(a,b)
