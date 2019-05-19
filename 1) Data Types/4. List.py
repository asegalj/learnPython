ls = [1, 2, 3, 4, 5]
print(ls[-2])
print(len(ls))


l1 = ls[2:4] 
l2 = ls[1:0]
l3 = ls[:3]
l4 = ls[0::2]
print(l1 , l2 , l3 , l4 )   

ls.append('a')
ls += ['danny' , 3.1]
ls[1:3] = ["hi" , 2]
print(ls)

ls.remove(1)
print(ls.pop())
print(ls)

