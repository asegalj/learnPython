print("Hello, world!")

str = "Ha"
str *= 4
print(str)

print(str.find('aHa'))
print(str.find('aha'))

print(str.lower().find('aha'))

str += '\n' + str + '\t' + str

print("""{0}""".format(str))
print(f"""{str}""")
if 'Ha' == "Ha"  == """Ha""":
    print("they are all equal")

