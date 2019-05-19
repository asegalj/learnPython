import argparse

def multiply(num1,num2):
    return num1*num2

def sub(num1,num2):
    return num1-num2

def add(num1,num2):
    return num1+num2

def divide(num1,num2):
    return num1/num2

def inputFunc():
    value=input("type exit: ")
    if(value=='exit'):
        return 'exit'
    elif(value=='+' or value=='-' or value=='*' or value=='/'):
        return value
    else:
        return (int)(value)

value = input("type exit: ")

while(True):
    num1 = inputFunc()
    if(num1=='exit'):
        break
    operand = inputFunc()
    if(operand=='exit'):
        break
    num2 = inputFunc()
    if(num2=='exit'):
        break
    if('+' == operand):
       result=add(num1,num2)
    if('-' == operand):
       result= sub(num1,num2)
    if('*' == operand):
       result= multiply(num1,num2)
    if('/' == operand):
       result=divide(num1,num2)
    print(result)
