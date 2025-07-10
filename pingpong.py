from pygame import * 
window = display.set_mode((700, 500))
display.set_caption("Ping Pong Game")
window.fill((52, 213, 235))

# make classes
class GameSprite(sprite.Sprite):
    def __init__(self, imagefile, x_position, y_position, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(imagefile), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# make object from classes

# game loop
