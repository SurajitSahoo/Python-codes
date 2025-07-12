marks1 = int(input("Enter the value of marks1: "))
marks2 = int(input("Enter the value of marks2: "))
marks3 = int(input("Enter the value of marks3: "))

total_percentge = (100*(marks1+marks2+marks3))/300

if(total_percentge>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed", total_percentge)
else:
    print("You are failled", total_percentge)    