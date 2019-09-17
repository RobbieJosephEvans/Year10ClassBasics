from random import randint

youguess = False
numtries = 0

correct = randint(0,1000)

#if(youguess.isdigit() == True):

while youguess == False:
    numtries = numtries + 1 
    #correct = randint(0,1000)
    print("Guess a number between 1-1000") 
    guess = input("Example: 200: ")
    numguess = int(guess) 
    if (numguess == correct): 
        str_tries =  str(numtries) 
        print("Well done!")
        print("You have solved the problem in " + str_tries + " tries.") 
        youguess = True 
    else:
        if (numguess > correct): 
              print("Wrong! Too high.")
        else:
            print("Wrong! Too low.")
        
else:
    print("You must enter a number")
