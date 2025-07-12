import math
n = float(input("Enter a number: "))

while True:
      if n==999:
         print ("not_possible")
         break
      elif n<0:
         print("this is a negative number")
         break
      else:
         sq_root = math.sqrt(n)
         print(f"The square root is: {sq_root}")   
         break


