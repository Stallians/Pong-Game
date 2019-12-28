# Simple Pong Game in Python3 for Beginners
# Part 6: Scoring

import turtle

window = turtle.Screen()
window.title('Pong by @stallians')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(n=1, delay=1)

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

# scoring
score_a = 0
score_b = 0

scorer = turtle.Turtle()
scorer.speed(0)
scorer.penup()
scorer.goto(0, 270)
scorer.hideturtle()
scorer.color('White')
scorer.write("Player 1:{}  Player 2:{}".format(score_a, score_b),align='center', font=('Courier',10, 'normal'))

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
        score_a +=1
        scorer.clear()
        scorer.write("Player 1:{}  Player 2:{}".format(score_a, score_b),align='center', font=('Courier',10, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        scorer.clear()
        scorer.write("Player 1:{}  Player 2:{}".format(score_a, score_b),align='center', font=('Courier',10, 'normal'))

    # ball and paddle collision
    if (ball.xcor() > 330 and ball.xcor() < 370) and (ball.ycor() > paddle_b.ycor()-40 and ball.ycor() < paddle_b.ycor()+40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -370) and (ball.ycor() > paddle_a.ycor()-40 and ball.ycor() < paddle_a.ycor()+40):
        ball.setx(-330)
        ball.dx *= -1
