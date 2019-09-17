from turtle import *
import random
#tracer(0, 0)

speed(10)

def foursquares():
    for p in range(4):
        for i in range(4):
            forward(100)
            right(90)
            #red = random.randint(0,255)
            #blue = random.randint(0,255)
            #green = random.randint(0,255)
            #begin_fill()
            #color((red,green,blue))
        forward(100)

    #goto(400,100)
    #goto(0,100)
    left(90)
    forward(100)
    left(90)
    forward(400)
    right(180)

foursquares()
foursquares()
foursquares()

for p in range(4):
    for i in range(4):
        forward(100)
        right(90)
    forward(100)

#update()
