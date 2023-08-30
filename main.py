from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()
scoreboard=ScoreBoard()
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(l_paddle.go_down, key="s")
screen.onkey(l_paddle.go_up, key="w")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with the r_paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #detect right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        print(f"LEFT SCORE:{scoreboard.l_point()}")
    #detect left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        print(f"RIGHT SCORE:{scoreboard.r_point()}")
    if scoreboard.l_score==10 or scoreboard.r_score==10:
        scoreboard.over()
        game_is_on=False


screen.exitonclick()
