from random import randint, random, randrange, choice

counter=1
MyValue=0
ComputerNumber = randint(1, 100)

while ComputerNumber!=MyValue and counter<=7 :
    MyValue = (int)(input(f"please guess the number:  {ComputerNumber}  "))
    if MyValue>ComputerNumber:
        print(f"your number is above ,you done {counter} tries")
    elif MyValue<ComputerNumber :
        print(f"your number is below ,you done {counter} tries")
    else:
        print(f"good you guessed the number is: {MyValue} in {counter}")
        break
    counter +=1
else:
        print(f"pc number is: {ComputerNumber}")
