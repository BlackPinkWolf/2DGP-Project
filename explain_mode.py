from pico2d import *
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode


def init():
    global image
    global bgm


    image = load_image('Aexplain.png')


    pass
def finish():
    pass
def update():

        pass
def draw():
    clear_canvas()
    image.clip_draw(0, 0, 1200, 630, 400, 300, 800, 600)
    update_canvas()
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            game_framework.change_mode(play_mode)

def pause():
    pass
def resume():
    pass