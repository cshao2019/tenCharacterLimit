f = open("input.txt", 'r')
input = f.readlines()
f.close()

f1 = open ("output.txt", 'w')

for characters in input:
	if len(characters) <= 10: #doesn't need it because \n already in input
		f1.write(characters)
		
	else:
		f1.write(characters[0:10])
		f1.write("\n") #only when characters more than 10 bc chopping off the new line too
		
	

		