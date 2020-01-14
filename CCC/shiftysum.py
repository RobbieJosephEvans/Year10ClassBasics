N = input("")

k = input("")

N = int(N)

k = int(k)

output = 0

for i in range(0,k+1,1):

	output = output + N*10**i

print(output)