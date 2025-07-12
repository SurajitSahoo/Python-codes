marks = int(input("Enter your marks: "))

if(marks<=100 & marks>=90):
    print("Your grade is E")
elif(marks<=89 & marks>=80):
    print("Your grade is A")   
elif(marks<=79 & marks>=70):
    print("Your grade is B")   
elif(marks<=69 & marks>=60):
    print("Your grade is C")   
elif(marks<=59 & marks>=50):
    print("Your grade is D")   
elif(marks<50):
    print("YOU ARE FAILED")   
else:
    print("BETTER LUCK NEXT TIME")
