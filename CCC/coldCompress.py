N = input("")
N = int(N)

counter = 0

for i in range(N):
	newinput = input()
	for i in newinput:
		if i in newinput:
			counter[i] += 1
			print(counter, newinput[i])
		else:
			counter[i] = 1
