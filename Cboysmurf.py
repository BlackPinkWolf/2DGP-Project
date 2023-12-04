# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT

import finish_mode
import game_world
from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, \
    draw_rectangle
import game_framework
import play_mode
import title_mode


# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3



class Idle:

    @staticmethod
    def enter(boy, e):
        boy.dir = 0
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 80, 0, 80, 137, boy.x, boy.y)



class Run:

    @staticmethod
    def enter(boy, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir = 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            boy.dir = -1

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if boy.x < 800 and boy.dir == 1:
            boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time * boy.speed
        if boy.x > 0 and boy.dir == -1:
            boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time * boy.speed
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 80, 0, 80, 137, boy.x, boy.y)

class Jump:

    @staticmethod
    def enter(boy, e):
        boy.dir = 0
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if boy.frame > 7:
            boy.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def draw(boy):
        if boy.frame < 1:
            boy.image_jump1.clip_draw(0, 0, 128, 163, boy.x, boy.y)
        elif boy.frame < 2:
            boy.image_jump2.clip_draw(0, 0, 107, 142, boy.x, boy.y)
        elif boy.frame < 3:
            boy.image_jump3.clip_draw(0, 0, 120, 134, boy.x, boy.y)
        elif boy.frame < 4:
            boy.image_jump4.clip_draw(0, 0, 120, 126, boy.x, boy.y)
        elif boy.frame < 5:
            boy.image_jump5.clip_draw(0, 0, 138, 195, boy.x, boy.y)
        elif boy.frame < 6:
            boy.image_jump6.clip_draw(0, 0, 147, 87, boy.x, boy.y)
        elif boy.frame < 7:
            boy.image_jump7.clip_draw(0, 0, 155, 115, boy.x, boy.y)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Jump},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Jump},
            Jump: {right_down: Run, left_down: Run, left_up: Run, right_up: Run,time_out: Idle}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)

class Boy:
    def __init__(self):
        self.x, self.y = 400, 500
        self.frame = 0
        self.dir = 0
        self.speed = 1
        self.heart = 1
        self.image = load_image('Aboy smurf run.png')
        self.image_jump1 = load_image('2-1.png')
        self.image_jump2 = load_image('2-2.png')
        self.image_jump3 = load_image('2-3.png')
        self.image_jump4 = load_image('2-4.png')
        self.image_jump5 = load_image('2-5.png')
        self.image_jump6 = load_image('2-6.png')
        self.image_jump7 = load_image('2-7.png')
        self.font = load_font('ENCR10B.TTF', 24)
        self.font1 = load_font('Cafe24Moyamoya-Face-v1.0.otf', 30)
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        self.state_machine.update()
        if self.heart == 0:
            game_framework.change_mode(finish_mode)


    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x - 40, self.y + 60, f'Speed:{self.speed:02d}', (255, 0, 0))
        self.font1.draw(50,  50, f'Time:{get_time()}', (100, 100, 100))
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-30,self.y-60,self.x+30,self.y+60

    def handle_collision(self,group,other):
        if group=='boy:item':
            self.speed +=1
        if group=='boy:tree' :
            self.heart -= 1
        if group == 'boy:rock' and self.state_machine.cur_state != Jump:
            self.heart -= 1