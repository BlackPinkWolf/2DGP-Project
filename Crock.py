import random
import math
import game_framework

from pico2d import *

import game_world

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0



class Rock:
    def __init__(self):
        self.image = load_image('Arock.png')
        self.x, self.y = random.randint(50, 750), random.randint(-1200, -100)
        self.speed = 3

    def update(self):
        self.y += RUN_SPEED_PPS * game_framework.frame_time * self.speed
        if self.y > 800:
            self.x, self.y = random.randint(50, 750), random.randint(-1200, -100)
        pass


    def draw(self):
        self.image.draw(self.x, self.y, self.image.w * 0.5, self.image.h * 0.5)


    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def handle_collision(self,group,other):
        if group == 'boy:rock' :
            pass
