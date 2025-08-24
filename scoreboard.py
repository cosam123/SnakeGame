from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())

        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  High score:{self.highscore}",align="center",font=("Arial",24,"normal"))
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w" ) as data:
                data.write(f"{self.score}")


        self.score=0
        self.update_score()



    def increase_score(self):
        self.score+=1

        self.update_score()
