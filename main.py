from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from structure import Structure
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(255, 239, 213)
screen.title("Snake game")
screen.tracer(0)

margins = Structure()
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

still_playing = True
while still_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        print("collision")
        food.refresh_position()
        score.increase()
        snake.extend()

    # detecting collision with the walls
    if snake.head.xcor() < -280 or snake.head.xcor() > 270 or snake.head.ycor() > 240 or snake.head.ycor() < -270:
        snake.reset()
        score.reset()
    # detecting collision with the tail
    for segment in snake.segments[1:]:  # skip the head, which is at position 0
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()

print(score.value)
screen.exitonclick()
