from pico2d import *

import game_world

import title_mode
import game_framework
from Cbackground1 import Background1
from Cbackground2 import Background2
from Cboysmurf import Boy
from Citem import Item
from Crock import Rock
from Ctree import Tree

# Game object class here


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global background1
    global background2
    global boy
    global tree
    global rock
    global item
    global bgm

    
    bgm = load_music('snow-132947.mp3')
    bgm.set_volume(64)
    bgm.play()



    background1 = Background1()
    game_world.add_object(background1, 0)

    background2 = Background2()
    game_world.add_object(background2, 0)

    boy = Boy()
    game_world.add_object(boy, 2)

    tree = [Tree() for _ in range(5)]
    game_world.add_objects(tree, 1)

    rock = [Rock() for _ in range(5)]
    game_world.add_objects(rock, 1)

    item = [Item() for _ in range(9)]
    game_world.add_objects(item, 1)

    game_world.add_collision_pair('boy:item', boy, None)

    for i in item:
        game_world.add_collision_pair('boy:item', None, i)

    game_world.add_collision_pair('boy:tree', boy, None)

    for t in tree:
        game_world.add_collision_pair('boy:tree', None, t)

    game_world.add_collision_pair('boy:rock', boy, None)

    for r in rock:
        game_world.add_collision_pair('boy:rock', None, r)


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
def finish():
    game_world.clear()
    pass
def pause():
    boy.wait_time=100000000000000000000000000000000.0
    bgm.pause()
    pass
def resume():
    boy.wait_time=get_time()
    bgm.resume()
    pass
