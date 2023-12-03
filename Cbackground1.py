from pico2d import load_image

class Background1:
    def __init__(self):
        self.image = load_image('Abackground snow resources.png')
        self.y=0

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, 400, 300+self.y, 800,600)

    def update(self):
        self.y+=1
        if self.y>=300:
            self.y=-300
        pass