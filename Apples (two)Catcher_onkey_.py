import turtle,random,time
import winsound # Import sound library

# Create Screen
wn=turtle.Screen()
wn.setup(700,700)
wn.tracer(2)  # make this process faster
wn.bgpic('Apple_Tree.gif')

score=turtle.Turtle()
score.hideturtle()
score.up()
score.color('blue')

def scr():
    score.goto(150,250)
    score.clear()           
    score.write ('Score=', font = ('Times New Roman',\
                                   20, 'bold'))
    score.goto(230,250)
    score.write (s, font = ('Times New Roman', 20, 'bold'))

#______________________________________________
# Create apple1 Image
apple1=turtle.Turtle()
image1='apple.gif'
wn.addshape(image1)
apple1.shape(image1)

# Create apple2 Image
apple2=turtle.Turtle()
image2='apple2.gif'
wn.addshape(image2)
apple2.shape(image2)
apple2.up()

# Create bowl Image
bowl=turtle.Turtle()
image2='bowl.gif'
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

s=0
def apple(turtle,rand):
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(-90)
    rand=random.randrange(-300,300)
    turtle.goto(rand,300)

delta1=1000
delta2=1000

def condition(turtle,delta):
    global s
    turtle.showturtle()
    turtle.fd(1)

    if turtle.ycor()<-300:
        turtle.hideturtle()
        turtle.goto(random.randrange(-300,300),300)
        turtle.showturtle()
    if delta <70:
        s=s+1
        turtle.hideturtle()
        frequency=1000 #Sound
        duration=100  # Sound
        winsound.Beep(frequency,duration) # Sound
        turtle.goto(random.randrange(-300,300),300)
        scr()
apple(apple1,random.randrange(-300,300))
apple(apple2,random.randrange(-300,300))
    
while True:
    delta1=abs(apple1.position()-bowl.position())
    delta2=abs(apple2.position()-bowl.position())
    condition(apple1,delta1)
    condition(apple2,delta2)
