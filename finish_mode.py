from pico2d import *
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode


def init():
    global image
    global bgm
    bgm = load_music('enchanted-chimes-177906.mp3')
    bgm.set_volume(64)
    bgm.play()

    image = load_image('Afinish.png')


    pass
def finish():
    pass
def update():

        pass
def draw():
    clear_canvas()
    image.clip_draw(0, 0, 1080, 554, 400, 300, 800, 600)
    update_canvas()
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def pause():
    pass
def resume():
    pass