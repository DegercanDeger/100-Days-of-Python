import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
starting_positions = [(0,0),(-20,0),(-40,0)]

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0,1)

    snake.move()
screen.exitonclick()

