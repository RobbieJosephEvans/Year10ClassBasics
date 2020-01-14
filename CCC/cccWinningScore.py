a1 = int(input(""))
a2 = int(input(""))
a3 = int(input(""))
a4 = int(input(""))
a5 = int(input(""))
a6 = int(input(""))

oneA = 3*a1
twoA = 2*a2
threeA = 1*a3

oneB = 3*a4
twoB = 2*a5
threeB = 1*a6

A = oneA + twoA + threeA

B = oneB + twoB + threeB

if A > B:
    print("A")
elif B > A:
    print("B")
elif A == B:
    print("T")
