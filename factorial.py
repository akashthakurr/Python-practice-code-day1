def fact(x):
    c=1
    for i in range(x,1,-1):
        c=c*i
    print("factorial of given number",c)


n=int(input("enter a number:"))
fact(n)

         
