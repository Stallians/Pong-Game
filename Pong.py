# Simple Pong Game in Python3 for Beginners
# Part 1: Game Window

import turtle

window = turtle.Screen()
window.title('Pong by @stallians')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

while True:
    window.update()