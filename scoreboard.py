from turtle import Turtle
with open("../../desktop/data.txt") as save:
    SCORE = int(save.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.up()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {SCORE}", False, "center", ('Courier', 16, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Courier', 18, 'normal'))
        with open("../../desktop/data.txt", "w") as save:
            global SCORE
            save.write(str(SCORE))

    def scored(self):
        self.clear()
        global SCORE
        SCORE += 1
        self.write(f"Score: {SCORE}", False, "center", ('Courier', 16, 'normal'))

