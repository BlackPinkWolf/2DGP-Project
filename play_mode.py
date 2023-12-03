from pico2d import *

import game_world

import title_mode
import game_framework
from Cbackground1 import Background1
from Cbackground2 import Background2
from Cboysmurf import Boy


# Game object class here


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            boy.handle_event(event)


def init():
    global background1
    global background2
    global boy


    background1 = Background1()
    game_world.add_object(background1, 0)

    background2 = Background2()
    game_world.add_object(background2, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
def finish():
    game_world.clear()
    pass
def pause():
    boy.wait_time=100000000000000000000000000000000.0
    pass
def resume():
    boy.wait_time=get_time()
    pass
