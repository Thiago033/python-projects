from   turtle import *
from   brick  import Brick
from   paddle import Paddle
from   ball   import Ball     
import time

#Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle = Paddle((0, -250))
ball = Ball((0, -200))
label = Turtle()

#label config
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")
label.goto(0, 0)
label.color("white")
label.penup()
label.hideturtle()

is_gaming = True

tx,ty = -250, 215
targets = []

for _ in range(5):
    for _ in range(10):
        target = Brick(tx, ty)
        targets.append(target)
        tx += 55
    ty -= 25
    tx = -250

while is_gaming:
    screen.update()
    
    ball.move()
    time.sleep(ball.move_speed)
    
    screen.onkey(paddle.go_left, 'Left')
    screen.onkey(paddle.go_right, 'Right')


    # -------------------------- COLLISIONS --------------------------
    #collision with paddle
    if ball.distance(paddle) < 40:
        ball.bounce_y()
    
    # collision with brick
    for target in targets:
        if ball.distance(target) < 40:
            ball.bounce_y()
            target.hideturtle()
            target.clear()
            target.destroyed = True
    
    # Right wall collision
    if ball.xcor() > 385:
        ball.bounce_x()

    # Left wall collision
    if ball.xcor() < -385:
        ball.bounce_x()
        
    # sky collision
    if ball.ycor() > 285:
        ball.bounce_y()
        
    # ground collsion
    if ball.ycor() < -285:
        is_gaming = False
        label.write("GAME OVER!", align=ALIGNMENT, font=FONT)
    
    #detect all bricks destroyed
    for target in targets:
        if target.destroyed == True:
            is_gaming = False
        else:
            is_gaming = True
            break
        
        if not is_gaming:
            label.write("YOU WON!", align=ALIGNMENT, font=FONT)
        
screen.exitonclick()
