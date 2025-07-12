a1 = int(input("Enter the value of a1: "))
a2 = int(input("Enter the value of a2: "))
a3 = int(input("Enter the value of a3: "))


if(a1>a2 and a1>a3):
    print(f"The greatest number is {a1}:")
if(a2>a1 and a2>a3):
    print("The greatest number is a2:", a2)
if(a3>a1 and a3>a2):
    print("The greatest number is a3:", a3)
#else:
    #print("Invailed")    