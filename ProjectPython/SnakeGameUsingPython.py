# Project 1 - Snake Game Using python by Tayyab
import turtle
import time
import random

delay = 0.1

# Screen Setting
wns = turtle.Screen()
wns.title("Snake Game By Tayyab")
wns.bgcolor("green")
wns.setup(width=600, height=600)
wns.tracer(0) # turn of all the updates

# Snake Head setting
head =turtle.Turtle()
head.speed(0) #animation speed not a moving speed
head.shape("square")
head.color("black")
head.penup() # moving backing no line draw
head.goto(0,0) # initial at the center
head.direction= "stop"

# Snake Food
food =turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup() # moving backing no line draw
food.goto(0,100) # initial at the center

# Snake Body ( Segment )
segments =[]


# Funtions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        
        head.setx(head.xcor() + 20)

# Keyboard listening
wns.listen()
wns.onkeypress(go_up,"w")
wns.onkeypress(go_down,"s")
wns.onkeypress(go_left,"a")
wns.onkeypress(go_right,"d")


# Main game loop
while True: # everytime its run and update the screen
    wns.update()
    
    # Checking for head collision to the food
    if head.distance(food)< 20:
        # move head through the food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # Add Segment to the body
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Move the end segment first in reverse order
        for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)

        # For First Segment move as head move
        if len(segments) >0:
            x=head.xcor()
            y=head.ycor()
            segments[0].goto(x,y)
    move()

    time.sleep(delay)

wns.mainloop()