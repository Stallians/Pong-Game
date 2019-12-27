# Simple Pong Game in Python3 for Beginners
# Part 4: Moving the Ball

import turtle

window = turtle.Screen()
window.title('Pong by @stallians')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Functions
def paddle_a_up():
    y_pos = paddle_a.ycor()
    y_pos += 20
    paddle_a.sety(y_pos)

def paddle_a_down():
    y_pos = paddle_a.ycor()
    y_pos -= 20
    paddle_a.sety(y_pos)

def paddle_b_up():
    y_pos = paddle_b.ycor()
    y_pos += 20
    paddle_b.sety(y_pos)

def paddle_b_down():
    y_pos = paddle_b.ycor()
    y_pos -= 20
    paddle_b.sety(y_pos)

# listen for key press: Key bindings
window.listen()
window.onkeypress(paddle_a_up,'w')
window.onkeypress(paddle_a_down,'s')
window.onkeypress(paddle_b_up,'Up')
window.onkeypress(paddle_b_down,'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
