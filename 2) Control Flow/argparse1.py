
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('num1', type=int)
parser.add_argument('operation')
parser.add_argument('num2', type=int)
args = parser.parse_args()
print(args)
num1 = args.num1
num2 = args.num2
operation = args.operation

def multiply(num1,num2):
    return num1*num2

def sub(num1,num2):
    return num1-num2

def add(num1,num2):
    return num1+num2

def divide(num1,num2):
    return num1/num2

if operation == '+':
   result = add(num1,num2)
elif operation == '-':
    result = sub(num1,num2)
elif operation == '*':
    result = multiply(num1,num2)
elif operation == '/':
    result = divide(num1,num2)



print(result)
