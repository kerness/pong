# Simple Pong Game

import turtle # basic graphic

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600) # 0,0 is on the center
window.tracer(0) #stops form update - speed game

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle() # turtle object
paddle_a.speed(0) # speed for animation - max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # strech the shape
paddle_a.penup() # draw a line
paddle_a.goto(-350, 0) # set on the left

# Paddle B
paddle_b = turtle.Turtle() # turtle object
paddle_b.speed(0) # speed for animation - max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # strech the shape
paddle_b.penup() # draw a line
paddle_b.goto(350, 0) # set on the left


# Ball
ball = turtle.Turtle() # turtle object
ball.speed(0) # speed for animation - max possible speed
ball.shape("square")
ball.color("white")
ball.penup() # draw a line
ball.goto(0, 0) # set on the left
ball.dx = -0.2 #delta x; change x every time ball moves int moves by 2px on x and y
ball.dy = 0.2

# Pen - score board
pen = turtle.Turtle()
pen.speed(0) # animation speed
pen.color("white")
pen.penup() # dont drive the line
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))



# some functions
def paddle_a_up():
    y = paddle_a.ycor() # returns the y coordinates
    y += 20 # add 20px
    paddle_a.sety(y) # set y to the new y

def paddle_a_down():
    y = paddle_a.ycor() # returns the y coordinates
    y -= 20 # add 20px
    paddle_a.sety(y) # set y to the new y

def paddle_b_up():
    y = paddle_b.ycor() # returns the y coordinates
    y += 20 # add 20px
    paddle_b.sety(y) # set y to the new y

def paddle_b_down():
    y = paddle_b.ycor() # returns the y coordinates
    y -= 20 # add 20px
    paddle_b.sety(y) # set y to the new y

# keyboard binding
window.listen() # listen for keyboard input
window.onkeypress(paddle_a_up, "w") # whe user press "w" call the function paddle_a_up
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up") # up arrow
window.onkeypress(paddle_b_down, "Down") # down arrow

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 # reverse the direction when reach the border
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1 # reverse the direction when reach the border

    if ball.xcor() > 390: #if off the screen
        ball.goto(0,0)
        ball.dx *= -1 # reverse direction
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))
    
    if ball.xcor() < -390: #if off the screen
        ball.goto(0,0)
        ball.dx *= -1 # reverse direction
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 # it bounces 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 # it bounces 