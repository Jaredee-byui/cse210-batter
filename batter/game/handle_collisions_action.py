
from game.action import Action
from game import ball
from game.audio_service import AudioService
from game import constants


class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service


    def execute(self, cast):
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        balls = cast["balls"]
        
        for brick in bricks:
            for ball in balls:
                if self._physics_service.is_collision(ball, brick):
                    self.check_collision(ball, brick)
                    bricks.remove(brick)
                if self._physics_service.is_collision(ball, paddle):
                    self.check_collision(ball, paddle)
            

    def check_collision(self, obj_1, obj_2):
        if self.check_vertical_collison(obj_1, obj_2):
            self.play_audio_bounce()
            obj_1.bounce_vertical()
        elif self.check_horizontal_collison(obj_1, obj_2):
            self.play_audio_bounce()
            obj_1.bounce_horizontal()


    def check_vertical_collison(self, ball, game_object):
        if ball.get_bottom_edge() >= game_object.get_top_edge():
            return True
        elif ball.get_top_edge() <= game_object.get_bottom_edge():
            return True


    def check_horizontal_collison(self, ball, game_object):
        if ball.get_left_edge() <= game_object.get_right_edge():
            return True
        elif ball.get_right_edge() >= game_object.get_left_edge():
            return True


    def play_audio_bounce(self):
        audio_service = AudioService()
        audio_service.play_sound(constants.SOUND_BOUNCE)
