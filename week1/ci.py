p=int(input("Enter the amount))
t=int(input("Enter the time))
r=int(input("Enter the interest rate))
a=p*(1+r/100)**t
ci=a-p
print(round(ci,2))
