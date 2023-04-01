a=eval(input("enter a number:"))
def count(a):
    c=n=0
    for i in range(len(a)):
          if a[i]%2==0:
              c+=1
          else:
              n=n+1
    return c,n
count(a)
        
    