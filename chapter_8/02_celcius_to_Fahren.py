def c_to_f(celsius):
   return (celsius*(9/5))+32

celsius = int(input("enter the celsius value: "))
print(round(c_to_f(celsius),2))