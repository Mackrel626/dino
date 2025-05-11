from objects import *
from settings import *

level1 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                    2                                 ",
    "                                 -----                                ",
    "  1                      -----                                        ",
    "-----               ---                                               ",
    "        o     ----                                                    ",
    "  o   -----                                                           ",
    "-----                                                                 ",
]


level2 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
]

level1_width = len(level1[0])*100
level1_heigth = len(level1)*30

level2_width = len(level2[0])*100
level2_heigth = len(level2)*30

level_objects = pygame.sprite.Group()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0,0, width, height)
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_config(camera, target_rect):
    l, t, _, _, =target_rect
    _, _, w, h, = camera

    l = min(0,l)
    l = max(-(camera.width - W), l)
    t = max(-(camera.heigth - H), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)
camera = Camera(camera_config, level1_width, level1_heigth) 

def draw_level(level: list):
    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 30, platform_image)
                level_objects.add(platform)
                platforms.add(platform)
            if symbol == "o":
                coin = MapObject(x, y, 100, 30, coin_image)
                level_objects.add(coin)
                coins.add(coin)
            if symbol == "1":
                key = MapObject(x, y, 100, 30, key_image)
                level_objects.add(key)
            if symbol == "2":
                chest = MapObject(x, y, 100, 30, chest_image)
                level_objects.add(chest)
            x +=100
        x =0
        y +=30
    return level_objects, key, chest