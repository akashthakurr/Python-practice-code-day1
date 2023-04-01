s=input("enter a string:")
l= len(s)
s2=''
for i in range(l):
    if i%2==0:
        s2=s2+s[i]
    else:
        pass
print(s2)
