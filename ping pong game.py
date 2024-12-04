from turtle import Screen
from class_for_ping_pong_game import Paddle
from Ballclass_for_ping_pong_game import Ball
from Scoreclass_for_ping_pong_game import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# Create game elements
r_paddle = Paddle((280, 0))  # Adjusted for consistency
l_paddle = Paddle((-280, 0))  # Adjusted for consistency
ball = Ball()
score = Scoreboard()

# Define game variables
winning_score = 5  # Set the winning score for the game

# Paddle controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Ball collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 260) or (ball.distance(l_paddle) < 50 and ball.xcor() < -260):
        ball.bounce_paddle()

    # Right player misses the ball
    if ball.xcor() > 300:
        ball.restart()
        score.l_point()

    # Left player misses the ball
    if ball.xcor() < -300:
        ball.restart()
        score.r_point()

    # Check for game over condition
    if score.l_score == winning_score or score.r_score == winning_score:
        game_is_on = False
        score.display_game_over()  # Display "Game Over" message


# Exit the game on click
screen.exitonclick()
