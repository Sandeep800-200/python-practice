n=int(input("enter the no of elemets in the list :-"))
l=[]
for i in range (n):
    a=int(input ("enter the number :-"))
    l.append(a)
lar = l [0]
for i in l :
    if i > lar :
        lar = i
print ('largest number in the list is ' , lar )


      