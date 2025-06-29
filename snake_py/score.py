from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Aria", 19, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.current_score =0
        self.update_score()


    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("Game over", align=ALIGNMENT, font=FONT)



