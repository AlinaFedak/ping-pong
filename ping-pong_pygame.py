from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, color = None):
        ().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
        self.fill_color = (200, 200, 255)
        if color:
            self.fill_color = color
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def fill(self):
        draw.rect(window, self.fill_color, self.rect)

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - sizey: #1235
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - sizey: #1235
            self.rect.y += self.speed
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

win_width = 700 #1280
win_height = 500 #700

sizey = 100
sizex = 20

dx = 3
dy = 3

window = display.set_mode((win_width, win_height))
window.fill((200, 200, 255))
display.set_caption("Пінг-понг")
# background = transform.scale(image.load("starry_sky.png"), (win_width, win_height))

# player1 = Player('platform.png', 10, 10, sizex, sizey, 10)
# player2 = Player('platform.png', 660, 10, sizex, sizey, 10)

ball = Player('ball.png', 100, 200, 50, 50, 10)

players = sprite.Group()
for i in range(1, 2):
    player = Player('platform.png', 10, 10, sizey, sizey, 10)
    players.add(player)
# players.add(player1)
# players.add(player2)

game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += dx
    ball.rect.y += dy
    
    if sprite.spritecollide(players, ball, False): #or sprite.spritecollide(player2, monsters, False) or lost>= 5:
        dx *= -1
    # if sprite.spritecollide(players, ball, False): #or sprite.spritecollide(player2, monsters, False) or lost>= 5:
    #     dx *= -1
    if ball.y < 0 or ball.y > win_height - 50: #or sprite.spritecollide(player2, monsters, False) or lost>= 5:
        dy *= -1

    # if ball.rect.colliderect(platform.rect):
    #     dy *= -1
    # if ball.rect.x < 0 or ball.rect.x > 450:
    #     dx *= -1

    # if ball.rect.y < 0:
    #     dy *= -1

    player.fill()
    player.fill()
    ball.fill()

    player.update2()
    player.update1()
    ball.update()

    player.reset()
    player.reset()
    ball.reset()

    player.draw()
    player.draw()
    ball.draw()

    display.update()
    time.delay(50)