
usefulA = a.split()

a1 = usefulA[0]

a1 = int(a1)

a2 = usefulA[1]

a2 = int(a2)

a3 = usefulA[2]

a3 = int(a3)

a4 = usefulA[3]

a4 = int(a4)

totalA = a1 + a2 + a3 + a4

#__________________________________________________

usefulB = b.split()

b1 = usefulB[0]

b1 = int(b1)

b2 = usefulB[1]

b2 = int(b2)

b3 = usefulB[2]

b3 = int(b3)

b4 = usefulB[3]

b4 = int(b4)

totalB = b1 + b2 + b3 + b4

#__________________________________________________

usefulC = c.split()

c1 = usefulC[0]

c1 = int(c1)

c2 = usefulC[1]

c2 = int(c2)

c3 = usefulC[2]

c3 = int(c3)

c4 = usefulC[3]

c4 = int(c4)

totalC = c1 + c2 + c3 + c4

#__________________________________________________

usefulD = d.split()

d1 = usefulD[0]

d1 = int(d1)

d2 = usefulD[1]

d2 = int(d2)

d3 = usefulD[2]

d3 = int(d3)

d4 = usefulD[3]

d4 = int(d4)

totalD = d1 + d2 + d3 + d4

if totalA == totalB == totalC == totalD:
    print("magic")
