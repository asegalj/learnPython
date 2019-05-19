ages = { 'Danny': 28, 'Alex': 27, 'Bob': 40 }
print(ages)
print(ages['Danny'])

ages['Ben'] = 43
print(ages)
del ages['Bob']
print(ages)

names = list(ages.keys())
print(names)

points = dict([(2.0, 3.0) , (4.0, 1.0) , (6.4, 3.2)])
print(points)