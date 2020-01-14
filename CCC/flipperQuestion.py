input1 = input("")

a = 1

b = 2

c = 3

d = 4

for i in range(0,len(input1)):
	if input1[i] == "H":
		a,c = c,a
		b,d = d,b
	if input1[i] == "V":
		a,b = b,a
		c,d = d,c

print(a, b)
print(c, d)