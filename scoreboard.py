from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
BIG_FONT = ("Aerial", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    # function to increase score everytime snake collides with food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    # function to display game over everytime snake head collides with the body/wall
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=BIG_FONT)