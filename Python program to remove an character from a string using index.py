s=input("enter a string:")
index=int(input("enter the index of character which you want to remove:"))
L=list(s)
l=len(L)
lst=[]
for i in range(l):
    if i!=index:
        lst.append(L[i])
    else:
        pass
s2=''
for k in range(len(lst)):
    s2=s2+lst[k]
print(s2)

        
        
    
