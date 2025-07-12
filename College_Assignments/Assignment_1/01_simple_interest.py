def si(p,t,r):
    return (p*t*r)/100
p = int(input("Enter principle value: "))
t = int(input("Enter time value: "))
r = int(input("Enter rate value: "))

print(f"The simple interrest is : {si(p,t,r)}")