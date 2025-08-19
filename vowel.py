s=input("eneter a string to count vowels :- ")
i=0
for char in s :
    if char == 'a' or char== 'e' or char =='i' or char =='o' or char== 'u' :
        i=i+1
print("there are ", i , "vovels in the string")
a,e,i,o,u = 0,0,0,0,0
for char in s :
    if char == 'a':
        a=a+1
    if char == 'e':
        e= e+1
    if char == 'i':
        i=i+1
    if char == 'o':
        o=o+1
    if char == 'u':
        u=u+1
if a > 0 :
    print("a occurs", a , "times")
if e > 0 :
    print ("e occurs", e , "times")
if i > 0 :
    print ("i occurs", i , "times")
if o > 0 :
    print ("o occurs", o , "times")
if u > 0:
    print ("u occurs", u , "times")