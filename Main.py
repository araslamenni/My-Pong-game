from turtle import Turtle, Screen

screen = Screen()
screen.title("My Pong game")
screen.bgcolor("black")
screen.setup(800, 600)


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y = paddle.ycor() + -20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.speed("fastest")
paddle.shapesize(stretch_wid=5, stretch_len=1)
# padel.turtlesize(stretch_wid=10, stretch_len=10)
x_pos = 350
y_pos = 0
paddle.goto(x_pos, y_pos)

screen.exitonclick()
