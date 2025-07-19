from turtle import Turtle


STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANS = 20

UP =90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake =[]
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        timmy_turtle = Turtle("square")
        timmy_turtle.color("white")
        timmy_turtle.penup()
        timmy_turtle.goto(position)
        self.snake.append(timmy_turtle)

    def extend (self):
        self.add_segment(self.snake[-1].position())


    def snake_move(self):

        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANS)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000,1000)

        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]



    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


