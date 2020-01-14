a = input("")
b = input("")
c = input("")
d = input("")
e = input("")
f = input("")

wins = 0
outcomes = [a, b, c, d, e, f]

for i in range(len(outcomes)):
	if outcomes[i] == "W":
		wins += 1

group = -1
if wins == 5 or wins == 6:
	group = 1
elif wins == 4 or wins == 3:
	group = 2
elif wins == 2 or wins == 1:
	group = 3

print(group)


# a = input("")

# b = input("")

# c = input("")

# d = input("")

# e = input("")

# f = input("")

# output = 0

# output = int(output)


# if a == "W":
# 	output = output + 1

# if b == "W":
# 	output = output + 1

# if c == "W":
# 	output = output + 1

# if d == "W":
# 	output = output + 1

# if e == "W":
# 	output = output + 1

# if f == "W":
# 	output = output + 1


# if output == 6:
# 	print("3")

# if output == 5:
# 	print("3")

# if output == 4:
# 	print("2")

# if output == 3:
# 	print("2")

# if output == 2:
# 	print("1")

# if output == 1:
# 	print("1")

# if output == 0:
# 	print("-1")