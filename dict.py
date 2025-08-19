s=  input (" enter a string;- ")
l = s.split()
frc = {}
for word in l :
    if word in frc:
        frc[word]+=1
    else:
        frc[word]=1
print("frequency of word in the textis as follows ",  frc)

