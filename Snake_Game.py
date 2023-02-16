# import required modules
import turtle
import time
import random
import os
import sys
 
turtle.register_shape("Body.gif")
turtle.register_shape("F_Down.gif")
turtle.register_shape("F_Up.gif")
turtle.register_shape("F_Left.gif")
turtle.register_shape("F_Right.gif")
turtle.register_shape("Crack_Land.gif")

grass=turtle.Turtle()
grass.shape("Crack_Land.gif")

writing=turtle.Turtle()

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
# the width and height can be put as user's choice
screen.setup(width=600, height=600)
screen.tracer(0)
segments=[]
# head of the snake
head = turtle.Turtle()
head.shape("F_Down.gif")
#head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
score=0
writing.hideturtle()
writing.penup()
writing.setpos(0,180)
writing.clear()
writing.write("Score="+str(score),font=("Calibri",30,"bold"))


# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'yellow'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)


def info():
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("black")
    # the width and height can be put as user's choice
    screen.setup(width=600, height=600)
    screen.tracer(0)
    segments=[]
    # head of the snake
    head = turtle.Turtle()
    head.shape("F_Down.gif")
    #head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    # Tail of snake
    tail=turtle.Turtle()
    tail.shape("Body.gif")
    tail.penup()


    # food in the game
    food = turtle.Turtle()
    colors = random.choice(['red', 'green', 'yellow'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)
 

 
# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        head.shape("F_Up.gif")
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        head.shape("F_Down.gif")
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        head.shape("F_Left.gif")
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        head.shape("F_Right.gif")
        x = head.xcor()
        head.setx(x+20)
 
 
         
screen.listen()
screen.onkeypress(goup, "Up")
screen.onkeypress(godown, "Down")
screen.onkeypress(goleft, "Left")
screen.onkeypress(goright, "Right")
 

while True:
    screen.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        
        screen.clear() 
        turtle.hideturtle()
        turtle.penup()
        turtle.setpos(-180,0)
        turtle.bgcolor("black")
        turtle.color("white")
        turtle.write("GAME OVER",font=("Calibri",60,"bold"))
        time.sleep(1)
        screen.bye()
        # Change Address to your Snake_Game.py Address
        os.system('python "E://Users//Rebel Singh//Desktop//Python_projects//Python_Teaching//5_Sujan_Coding_Classes//Class25_Snake_Game//6_Snake_Game6.py')
        
        head.goto(0, 0)
        head.direction = "Stop"        
       
        
    if head.distance(food) < 20:
        score=score+1
        writing.hideturtle()
        writing.penup()
        writing.setpos(0,180)
        writing.clear()
        writing.write("Score="+str(score),font=("Calibri",30,"bold"))
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        
        
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.goto(1000,1000)
        new_segment.shape("Body.gif")
        new_segment.speed(0)
        segments.append(new_segment)
        

      
    
           
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
       
        
    if len(segments) > 0:
        
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
 
        

    move()
    time.sleep(0.1)
    
screen.mainloop()
   
