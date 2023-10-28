from pico2d import load_image

class Snow:
    def __init__(self):
        self.image = load_image('background snow resources.png')

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, 400, 300, 800,600)

    def update(self):
        pass