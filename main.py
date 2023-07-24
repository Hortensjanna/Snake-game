from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('yellow green')
screen.title('My Snake Game')

snake_segment_position = [(0, 0), (-20, 0), (-40, 0)]
for snake_segment in range(3):
    new_snake_segment = Turtle(shape='square')
    new_snake_segment.color('gray20')
    new_snake_segment.setposition(snake_segment_position[snake_segment])


























screen.exitonclick()
