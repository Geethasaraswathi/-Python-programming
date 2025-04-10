def createlist(l,n):
    for i in range(n):
        temp=int(input("Enter the list :"))
        l.append(temp)
    return l
n1=int(input("Enter the limit n1"))
n2=int(input("Enter the limit n2"))
n3=int(input("Enter the limit n3"))
l1=[]
l2=[]
l3=[]
l1=createlist(l1,n1)
print(l1)
l2=createlist(l2,n2)
print(l2)
l3=createlist(l3,n3)
print(l3)
