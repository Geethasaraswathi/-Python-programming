x=int(input("Enter a number"))
flag=0
for i in range(2,x):
    if(x%i==0):
       print("not a prime number")
       flag=1
       break;
else:
    if(flag==0):
       print("is a prime number")
        
