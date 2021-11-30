from turtle import Turtle

FONT = ("Courier", 24, "normal") # font to write the score board


class Scoreboard(Turtle):
    '''
    This Scoreboard is going to write the level we are currently on and the GAME OVER sequence
    '''

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        # self.name()

    def update_scoreboard(self):
        '''
        This method write and update the score board
        '''
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        '''
        This method increase the level of the game on the scoreboard
        '''
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        '''
        This method write GAME OVER when the game over.
        '''
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
    # def name(self):
    #     '''
    #     This method write GAME OVER when the game over.
    #     '''
    #     self.goto(290, -290)
    #     self.write(f"By Uthman", align="right", font=("Courier", 12, "normal"))
