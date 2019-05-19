while True:
    print("looping")
    break

count = 1
while count <= 4:
    print("looping")
    count += 1
    print(f"We're counting odd numbers: {count}")

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)
print(color)

for color in colors:
    if color == 'blue':
       continue
    elif color == 'red':
        break
    print(color)

for letter in "my_string":
    print(letter)

ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")