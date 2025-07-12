ok=[]
list = ['abc', 'xyz', 'aba', '1221']
for i in list:
	if(len(i)>=2 and i[0]==i[len(i)-1]):
		ok.append(i)
print("The list is: ", ok)
print("The number is: ",len(ok))
