from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('yellow green')
screen.title('My Snake Game')
screen.tracer(0)

snake_segment_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in snake_segment_position:
    new_snake_segment = Turtle(shape='square')
    new_snake_segment.color('gray20')
    new_snake_segment.penup()
    new_snake_segment.goto(position)
    segments.append(new_snake_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
