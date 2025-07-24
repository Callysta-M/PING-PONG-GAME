from pygame import * 
window = display.set_mode((700, 500))
display.set_caption("Ping Pong Game")
window.fill((52, 213, 235))

clock = time.Clock()
FPS = 30
score1 = 0
score2 = 0

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

class Player(GameSprite):
    def update_c1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

    def update_c2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

speedx = 5
speedy = 5

class Ball(GameSprite):
    def update_ball(self, speedx, speedy):
        self.rect.y += speedy #for movement
        self.rect.x += speedx

player1 = Player("Racket (1).png", 20, 200, 10, 25, 80)
player2 = Player("Racket (1).png", 655, 200, 10, 25, 80)
ball = Ball("Tennisball (1).png",320, 200, 10, 30, 30)

font.init()
font1 = font.SysFont(None, 70)
font2 = font.SysFont(None, 25)

#winning p1 text
player1_win= font1.render('PLAYER 1 WINS!', True, (255, 215, 0))

#wining p2 text
player2_win= font1.render('PLAYER 2 WINS!', True, (255, 0, 0))
# make object from classes

# game loop
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        window.fill((52, 213, 235))
        player1.show()
        player1.update_c1()
        player2.show()
        player2.update_c2()
        ball.show()

        score_p1 = font2.render('Score player 1: ' + str(score1), True, (0, 0, 0))
        score_p2 = font2.render('Score player 2: ' + str(score2), True, (0, 0, 0))
        window.blit(score_p1, (20, 20))
        window.blit(score_p2, (540, 20))

        if ball.rect.y >= 470 or ball.rect.y <= 0:
            speedy *= -1

        #player 1 plus score
        if ball.rect.x >= 670:
            ball.rect.x = 320
            ball.rect.y = 200
            score1 += 1

        #player 2 plus score
        if ball.rect.x <= 0:
            ball.rect.x = 320
            ball.rect.y = 200
            score2 += 1

        if score1 > 3:
            finish = True
            window.blit(player1_win, (170, 200))

        if score2 > 3:
            finish = True
            window.blit(player2_win, (170, 200))

        #ball collide with player
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speedx *= -1
            speedy *= -1

        ball.update_ball(speedx, speedy)

    else:
        time.delay(2000)
        finish = False
        ball.rect.x = 320
        ball.rect.y = 200
        score1 = 0
        score2 = 0
        player1.rect.x = 20
        player1.rect.y = 200
        player2.rect.x = 650
        player2.rect.y = 200

    display.update()
    clock.tick(FPS)
