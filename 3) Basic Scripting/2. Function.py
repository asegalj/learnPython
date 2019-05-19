def hello_world():
    print("Hello, World!")

def sum(list_of_numbers):
    sum = 0
    for num in list_of_numbers:
        sum += num
    return sum

print(sum({1,2,3,4,5}))