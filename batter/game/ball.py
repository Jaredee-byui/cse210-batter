from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    def __init__(self):
        super().__init__()
        # self.set_position(Point(0, 0))
        self.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))
        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        self.set_image(constants.IMAGE_BALL)

    def bounce_horizontal(self):
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        return self.set_velocity(Point(-dx, dy))

    def bounce_vertical(self):
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        return self.set_velocity(Point(dx, -dy))