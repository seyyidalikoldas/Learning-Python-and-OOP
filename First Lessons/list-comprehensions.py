
numbers = [x for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10)]
print(numbers)

years = [1983, 1999, 2008, 1956, 1986]
ages = [2023-year for year in years]
print(ages)

results = [x if x%2==0 else "Tek" for x in range(1,10)]
print(results)

result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
