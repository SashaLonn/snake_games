from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Aria", 19, "normal")
PATH = "data.txt"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.current_score =0
        self.manage_file()
        self.high_score = int (self.manage_file())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.update_score()

    def manage_file(self):
        with open(PATH,mode="r") as file:
           return file.read()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open(PATH, mode="w") as file:
                 file.write(str(self.high_score))
        self.current_score =0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write("Game over", align=ALIGNMENT, font=FONT)



