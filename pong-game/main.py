from    turtle      import  Screen
from    paddle      import  Paddle
from    ball        import  Ball
from    scoreboard  import  Scoreboard        
import  time

#Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

is_gaming = True


while is_gaming:
    screen.update()
    
    ball.move()
    time.sleep(ball.move_speed)
    
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    

    #Detect collision with wall 
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        

    #Right collision
    if ball.xcor() > 385:
        ball.reset_position()
        ball.bounce_paddle()
        scoreboard.l_point()

    #Left collision
    if ball.xcor() < -385:
        ball.reset_position()
        ball.bounce_paddle()
        scoreboard.r_point()

screen.exitonclick()
