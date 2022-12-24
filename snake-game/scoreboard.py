from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('projects\snake-game\data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
    
         
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    
    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open('projects\snake-game\data.txt', 'w') as file:
                file.write(str(self.high_score))
            
        self.score = 0
        self.update_scoreboard()
