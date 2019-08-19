import turtle
import random
import time
import winsound # Import sound library

# Create Screen
wn=turtle.Screen()
wn.setup(700,700)
wn.tracer(2)  #to make this process faster
wn.bgpic('Apple_Tree.gif')

score=turtle.Turtle()
score.hideturtle()
score.up()
score.color('blue')

def scr():
    score.goto(150,250)
    score.clear()           
    score.write ('Score=', font = ('Times New Roman', 20, 'bold'))
    score.goto(230,250)
    score.write (s, font = ('Times New Roman', 20, 'bold'))

# Create apple Image
apple=turtle.Turtle()
image1='apple.gif'
wn.addshape(image1)
apple.shape(image1)
apple.hideturtle()
apple.showturtle()

# Create apple2 Image
apple2=turtle.Turtle()
image2='apple.gif'
wn.addshape(image2)
apple2.shape(image2)
apple2.hideturtle()
apple2.showturtle()

# Create bowl Image
bowl=turtle.Turtle()
image2='b.gif'
wn.addshape(image2)
bowl.shape(image2)
bowl.hideturtle()
bowl.penup()
bowl.goto(0,-300)
bowl.showturtle()

def left():
    bowl.fd(-50)
def right():
    bowl.fd(50)

turtle.onkey(left,"Left")
turtle.onkey(right, "Right")
turtle.listen()

q1=0
q2=0
s=0
apple.hideturtle()
apple.penup()
apple.setheading(-90)
a=random.randrange(-300,300)
apple.goto(a,300)

apple2.hideturtle()
apple2.penup()
apple2.setheading(-90)
a2=random.randrange(-300,300)
apple2.goto(a2,300)

while True:
    q1=q1+1
    apple.showturtle()
    apple.fd(1)

    q2=q2+1
    apple2.showturtle()
    apple2.fd(1)
    
    delta=abs(apple.position()-bowl.position())
    delta2=abs(apple2.position()-bowl.position())

    if q1>700:
        q1=0
        apple.hideturtle()
        a=random.randrange(-300,300)
        apple.goto(a,300)

    if q2>700:
        q2=0
        apple2.hideturtle()
        a2=random.randrange(-300,300)
        #apple2.fd(1)
        apple2.goto(a2,300)

    if delta <70:
        s=s+1
        apple.hideturtle()
        a=random.randrange(-300,300)
        frequency=1000 #Sound
        duration=100  # Sound
        winsound.Beep(frequency,duration) # Sound
        q1=0
        apple.goto(a,300)
        scr()

    if delta2 <70:
        s=s+1
        apple2.hideturtle()
        a2=random.randrange(-300,300)
        frequency=1000 #Sound
        duration=100  # Sound
        winsound.Beep(frequency,duration) # Sound
        q2=0
        apple2.goto(a2,300)
        scr()
        
