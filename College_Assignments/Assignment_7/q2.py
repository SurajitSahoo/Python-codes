topper_details = (
    ("Surajit", "Mathematics", 95),
    ("Abhijit", "Physics", 92),
    ("souvik", "Chemistry", 90)
)

def display_topper_details(toppers):
    print("Topper Details:")
    for topper in toppers:
        print(f"Name: {topper[0]}, Subject: {topper[1]}, Marks: {topper[2]}")


display_topper_details(topper_details)


topper_list = list(topper_details)


topper_list[2] = ("souvik", "Chemistry", 95)  
topper_list[1] = ("Abhijit", "Mathematics", 97) 

topper_details = tuple(topper_list)


print("\nUpdated Topper Details:")
display_topper_details(topper_details)
