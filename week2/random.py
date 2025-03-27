import random
n=random.randint(1,10)
while True:
     x=int(input("Enter any number"))
     if(x<n):
         print("Number is too low")
     elif(x>n):
         print("Number is too high")
     else:
         print(" same number")

 
