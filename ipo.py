while True:
    x = input("enter number you want to be squared:")
    if(x.isdigit() == True):
        x = int(x)
        print(x*x)
    elif int(x) < 0:
        x = int(x)
        print(x*x)
    else:
        print("You did not enter a number")
