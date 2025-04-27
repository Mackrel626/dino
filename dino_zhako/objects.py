from settings import *

class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.widht =width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.x =x 
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__()
        self.widht =width
        self.height = height
        self.anim_count = 0
        self.images = images 
        self.image = pygame.transform.scale(self.images[self.anim_count], (width, height))

        self.rect = self.image.get_rect()
        self.rect.x =x 
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__(x, y, width, height, speed, images)
        self.action='idle'
        self.animation={
            'idle': list(range(4)),
            'right': list(range(4,10)),
            'left': list(range(10, 17))
        }

'''дописати'''