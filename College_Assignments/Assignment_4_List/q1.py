final_list = []
duplicate =[2,4,5,7,2,4]
for num in duplicate:
    if num not in final_list:
        final_list.append(num)
print("The list is: ",final_list)
