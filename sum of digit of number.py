#sum of digit of number
a= int(input("enter the number:"))
s=str(a)
l=len(s)
r=0
for i in range(l):
    r=r+int(s[i])
print("sum of digits of given number is",r)

    
