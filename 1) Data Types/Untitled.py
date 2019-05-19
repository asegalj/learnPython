dict1 = {"ofer":21,"shimon":21 ,'Danny': 7, 'Alex': 21, 'Bob': 40 }

def isThereTheLetterO(name):
    isCheck = 'o'in name == 1;
    return isCheck

for name,id in dict1.items():
    if(isThereTheLetterO(name) or id%7==0 ):
        print(name)

