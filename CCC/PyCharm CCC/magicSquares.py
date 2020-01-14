a = input("")
b = input("")
c = input("")
d = input("")

list = [a,b,c,d]
list2 = [a,b,c,d]

counter = 0

for i in range(0,4,1):

    usefulA = list[i].split()

    a1 = usefulA[0]

    a1 = int(a1)

    a2 = usefulA[1]

    a2 = int(a2)

    a3 = usefulA[2]

    a3 = int(a3)

    a4 = usefulA[3]

    a4 = int(a4)

    list2[i] = a1 + a2 + a3 + a4

if a == b == c == d:
    print("magic")
else:
    print("not magic")

