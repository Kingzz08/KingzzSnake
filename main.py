from turtle import Screen, Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# setting up screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Classic Snake")
screen.tracer(0)

# create snake, food, scoreboard object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen keystrokes from keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# Game Starts
while game_is_on:

    # updates the screen and sets speed and allows the snake to move by calling move().
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_size()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail/body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
