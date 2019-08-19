import turtle
import random
import winsound # Import sound library

# Create Screen
wn=turtle.Screen()
wn.setup(700,700)
#wn.tracer(2)  #to make this process faster
wn.bgpic('Apple_Tree.gif')

score=turtle.Turtle()
score.hideturtle()
score.up()
score.color('blue')

# Create apple Image
apple=turtle.Turtle()
image1='apple.gif'
wn.addshape(image1)
apple.shape(image1)
apple.hideturtle()
apple.showturtle()

# Create bowl Image
bowl=turtle.Turtle()
image2='b.gif'
wn.addshape(image2)
bowl.shape(image2)
bowl.hideturtle()
bowl.penup()
bowl.goto(0,-300)
bowl.showturtle()

q=0
s=0
apple.setheading(-90)
apple.penup()
apple.hideturtle()
a=random.randrange(-300,300)
apple.goto(a,300)
while True:
    q=q+1
    apple.showturtle()
    apple.fd(32) #motion down
    if q>19:
        q=0
        apple.hideturtle()
        a=random.randrange(-300,300)
        apple.goto(a,300)
 
    position1=apple.position()
    position2=bowl.position()
        #print(position2)
    delta=abs(position1-position2)
        
    if delta <70:
        s=s+1  #Score
        apple.hideturtle()
        a=random.randrange(-300,300)
        frequency=1000 #Sound
        duration=100  # Sound
        winsound.Beep(frequency,duration) # Sound

 # Score on the Screen with position (x=150, y=250)
 # Score number position x=230, y=250
            
        score.goto(150,250)
        score.clear()
        score.write ('Score=', font = ('Times New Roman', 20, 'bold'))
        score.goto(230,250)
        score.write (s, font = ('Times New Roman', 20, 'bold'))
        apple.goto(a,300)
        q=0

#wn.onclick(bowl.goto)# Control of the bowl position
    def left():
        bowl.fd(-50)
    def right():
        bowl.fd(50)
    turtle.onkey(left,"Left")
    turtle.onkey(right, "Right")
    turtle.listen()
            
        


        
            

         
    
   





        


