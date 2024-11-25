from paddle import Paddle
from ball import Balls
from lifes import Life
from score import Score
from screen import Screen
from titles import Titles

class Breakout:
    def __init__(self):
        self.screen = Screen(800, 600, 200, 100)
        self.paddle = Paddle(400, 550, 100, 10, 0, None)  
        self.ball = Balls(50, 100, 0, 0, 0, (255,255,255))  
        self.lives = Life(3)  
        self.score = Score(0)  

        self.titles = Titles(50, 20, 0, 0, "blue", 10, 5, None)
        self.titles = Titles(50, 20, 10, 10, "red", 10, 5, None)
        self.titles = Titles(50, 20, 20, 20, "green", 10, 5, None)
        self.titles = Titles(50, 20, 30, 30, "yellow", 10, 5, None)

        self.running = True
        self.start_screen_active = True


    def game_startup(self):
        '''Resets everything inside the game'''
        self.lives.reset_life()
        self.score.reset_score()
        self.titles.undestroy_bricks()
        
    def run_game(self):
        while self.running == True:
            self.check_events()
            self.draw()
        
    def draw(self):
        self.paddle.draw_paddle(self.screen)  
        self.ball.draw_ball(self.screen) 
        self.lives.show_life(self.screen)  
        self.score.show_score(self.screen)  
        self.titles.draw_bricks()
        
    def check_events(self):


    def update_events(self):
        
        
    def start_screen(self,bool):