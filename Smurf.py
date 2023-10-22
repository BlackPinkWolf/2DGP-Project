# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT


class Smurf:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('boy smurf resources.png')

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100,100, 100, 100, self.x, self.y)
        pass
