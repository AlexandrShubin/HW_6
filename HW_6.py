# Задача: предложить улучшения кода для уже решённых задач. 
# ПЯТЬ ШТУК:

# С помощью использования **лямбд, filter, map, zip, enumerate, 
# list comprehension

my_matr = [
    [5, 15, 25],
    [10, 20, 30],
    [15, 20, 25]]
          
result = []
for row in my_matr:
    for item in row:
        item *= 14.5

result = map(lambda x: x * 2.8, my_matr)

result = [item * 2.8 for row in my_matr for item in row]

print(my_matr)

result = []
summ = 0
for row in my_matr:
    summ = sum(row)
    if summ < 10:
        result.append(row)

result = filter(lambda x: sum(x) < 10, my_matr)

result = [row for row in my_matr if sum(row) < 10]

print(my_matr)

result = []
for row in my_matr:
    for item in row:
        result.append(item)

result = [item for row in my_matr for item in row]

print(my_matr)