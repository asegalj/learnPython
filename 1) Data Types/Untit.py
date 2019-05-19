flag=True
i=2
j=2
while i<=10:
    while j<i:
        if i%j==0:
            flag=False           
            break  
        j+=1  
    if flag==False:
        print(str(i) + " not a prime")
    else:
        print(i) 
    j=2  
    i+=1
    flag=True
   
        
            
    
        