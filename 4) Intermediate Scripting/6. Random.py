from random import randint, random, randrange, choice
print("Printing random number using random.random()")
print(random())

print("Printing random integer ", randint(0, 9))
print("Printing random integer ", randrange(0, 10, 2))

Lectures_list = ['Python', 'Docker', 'Git', 'CI', 'k8s']
print("Select random element from list - ", choice(Lectures_list))