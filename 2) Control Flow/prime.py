flag=True
i=2
while i<=10:
    for j in range(2,i):
        if i%j==0:
            flag=False           
            break  
    if flag==False:
        print(str(i) + " not a prime")
    else:
        print(i)   
    i+=1
    flag=True