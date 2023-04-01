l=eval(input("enter a list of strings to compare:"))
larger=l[0]
for i in l:
    if len(i)>len(l[0]):
        larger=i
    else:
        pass
print(larger)


    
        
