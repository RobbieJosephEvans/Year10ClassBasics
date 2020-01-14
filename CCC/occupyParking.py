N = input("")

N = int(N)

y = input("")

t = input("")

doubleOccupied = 0

for i in range(0,N):
	if y[i] == t[i]:
		if y[i] == "C":
			doubleOccupied = doubleOccupied + 1

print(doubleOccupied)