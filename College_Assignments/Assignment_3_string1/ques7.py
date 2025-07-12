v_count = 0
c_count = 0

n = "umbrella"
for i in n:
	if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' :
		v_count +=1
	else:
		c_count +=1
print(f"The number of vowels: {v_count}")
print(f"The number of conconant :{c_count}")
