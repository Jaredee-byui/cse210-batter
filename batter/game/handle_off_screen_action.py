from game import constants
from game.action import Action

class HandleOffScreenAction(Action):
    """Code template for the rules that govern the interaction of the ball and the game window.
    
    Stereotype:
        Controller

    Attributes:
        none
    """
    def __init__(self):
        super().__init__()
    

    def execute(self, cast):
        '''
        exectues the functionality of the class, handles calls to check border collisions. 

        attributes:
            cast, the collection of all actors in play.
        
        '''

        ball = cast["balls"][0]
        if self.check_bounce_horizontal(ball) == True:
            ball.bounce_horizontal()
        if self.check_bounce_vertical(ball) == True:
            ball.bounce_vertical()
        elif self.check_bounce_vertical(ball) == False:
            ball.bounce_vertical()
            cast["balls"].remove(ball)


    def check_bounce_horizontal(self, ball):
        '''
        checks for an interaction between the balls horizontal edges and the horizontal edges of the game window.
        '''
        if ball.get_left_edge() <= 0 or ball.get_right_edge() >= constants.MAX_X:
            return True
        

    def check_bounce_vertical(self, ball):
        if ball.get_top_edge() <= 0:
            return True
        elif ball.get_bottom_edge() >= constants.MAX_Y:
            return False