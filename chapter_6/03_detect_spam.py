p1="make a lot of money"
p2="buy now"
p3="ubcribe this"
p4="click this"

massege=input("Enter your massege")

if((p1 in massege) or (p2 in massege) or (p3 in massege) or (p4 in massege)):
    print("Thi comment is spam")
else:
    print("This comment is not spam")    