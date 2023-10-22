from pico2d import *

import Game_World
from Smurf import Smurf


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            smurf.handle_event(event)


def reset_world():
    global running
    global smurf

    running = True

    smurf = Smurf()
    Game_World.add_object(smurf, 0)


def update_world():
    Game_World.update()


def render_world():
    clear_canvas()
    Game_World.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
