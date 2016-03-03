f = open("input.txt", 'r')
input = f.read()
f.close()

f1 = open ("output.txt", 'w')
f1.write(input)
f1.close()